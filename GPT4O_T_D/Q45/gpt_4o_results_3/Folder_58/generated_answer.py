from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    english_letters = [c for c in s[0:7] if c.isalpha()]
    palindromes = set()
    for perm in permutations(english_letters):
        perm_str = ''.join(perm)
        if len(perm_str) >= 6:
            for i in range(len(perm_str) - 5):
                for j in range(i + 6, len(perm_str) + 1):
                    substr = perm_str[i:j]
                    if substr == substr[::-1]:
                        palindromes.add(substr)
    return palindromes