from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters = [c for c in s[1:8] if c.isalpha()]
    unique_palindromes = set()
    for perm in permutations(letters):
        candidate = ''.join(perm)
        if len(candidate) >= 5:
            for length in range(5, len(candidate) + 1):
                sub_candidate = candidate[:length]
                if sub_candidate == sub_candidate[::-1]:
                    unique_palindromes.add(sub_candidate)
    return unique_palindromes