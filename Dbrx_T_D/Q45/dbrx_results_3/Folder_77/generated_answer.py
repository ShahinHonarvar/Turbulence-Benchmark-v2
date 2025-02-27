from collections import defaultdict

def palindromes_between_indices(text):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(4, 7):
        for j in range(i, 7 - i + 1):
            substr = text[i:j + 1]
            substr = ''.join((c.lower() for c in substr if c.lower() in english_letters))
            if len(substr) == j - i + 1 and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes