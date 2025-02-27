from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = s[5:10].lower()
    letters = set(substr) & english_letters
    if len(letters) < 2:
        return set()
    palindromes = set()
    for length in range(5, len(substr) + 1):
        for i in range(len(substr) - length + 1):
            subsub = substr[i:i + length]
            if len(subsub) == len(set(subsub) & letters) and subsub == subsub[::-1]:
                palindromes.add(subsub)
    return palindromes