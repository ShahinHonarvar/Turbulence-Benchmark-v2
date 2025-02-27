from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:7].lower()
    letters = [c for c in s if c.isalpha()]
    possible_palindromes = set()
    for perm in permutations(letters, len(letters)):
        perm_str = ''.join(perm)
        for length in range(3, len(perm_str) + 1):
            for start in range(len(perm_str) - length + 1):
                substr = perm_str[start:start + length]
                if substr == substr[::-1]:
                    possible_palindromes.add(substr)
    return possible_palindromes