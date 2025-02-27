from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = s[2:6].lower()
    letters = set(substr) & english_letters
    if len(letters) < 2:
        return set()
    palindromes = set()
    for length in range(4, len(substr) + 1):
        for i in range(len(substr) - length + 1):
            candidate = substr[i:i + length]
            if len(candidate) == len(set(candidate)) and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes