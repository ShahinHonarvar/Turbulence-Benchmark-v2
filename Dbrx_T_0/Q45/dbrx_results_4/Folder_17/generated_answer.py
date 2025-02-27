from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = s[2:7].lower()
    possible_letters = set(substr) & english_letters
    palindromes = set()
    if len(possible_letters) < 2:
        return palindromes
    for length in range(4, len(substr) + 1):
        for i in range(len(substr) - length + 1):
            candidate = substr[i:i + length]
            if len(candidate) == len(set(candidate)) and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes