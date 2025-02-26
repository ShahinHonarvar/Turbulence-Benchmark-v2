from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:10] if c.isalpha()]
    unique_palindromes = set()
    for length in range(5, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            candidate = ''.join(perm)
            if len(set(candidate)) < 2:
                continue
            for i in range(len(candidate)):
                reversed_candidate = candidate[::-1]
                if candidate == reversed_candidate:
                    unique_palindromes.add(candidate)
                    break
    return unique_palindromes