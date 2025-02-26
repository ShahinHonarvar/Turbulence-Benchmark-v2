from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:10] if c.isalpha()]
    unique_palindromes = set()
    for length in range(7, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for candidate in [''.join(p) for p in [perm + perm[-2::-1]]]:
                if len(candidate) >= 7 and candidate == candidate[::-1]:
                    unique_palindromes.add(candidate)
    return unique_palindromes