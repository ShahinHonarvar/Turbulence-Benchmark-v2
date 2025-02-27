from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    substring = s[6:9].lower()
    english_letters = [ch for ch in substring if ch.isalpha()]
    palindromes_set = set()
    for perm in permutations(english_letters):
        perm_str = ''.join(perm)
        for i in range(3, len(perm_str) + 1):
            for j in range(len(perm_str) - i + 1):
                sub_perm = perm_str[j:j + i]
                if sub_perm == sub_perm[::-1]:
                    palindromes_set.add(sub_perm)
    return palindromes_set