from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substr = s[6:9]
    letters = set(substr) & english_letters
    palindromes = set()
    if len(letters) < 2:
        return palindromes
    for i in range(4, len(substr) + 1):
        for j in range(len(substr) - i + 1):
            candidate = substr[j:j + i]
            if len(candidate) == len(set(candidate) & english_letters) and candidate == candidate[::-1]:
                palindromes.add(candidate.lower())
    return palindromes