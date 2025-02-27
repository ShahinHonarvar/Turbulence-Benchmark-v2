from itertools import permutations

def palindromes_between_indices(s):
    substr = s[4:10]
    english_letters = [ch for ch in substr.lower() if ch.isalpha()]
    palindromes = set()
    for perm in permutations(english_letters):
        perm_str = ''.join(perm)
        if len(perm_str) >= 6 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes