from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    if len(s) < 4:
        return palindromes
    for i in range(2, 4):
        candidates = defaultdict(int)
        for j in range(i - 2, len(s) - 2):
            substring = s[j + 2:j + 4].lower()
            if all((char in english_letters for char in substring)):
                candidates[substring] += 1
                palindromes.update((pal for pal in candidates.keys() if len(pal) >= 3 and candidates[pal] > 0))
    return palindromes