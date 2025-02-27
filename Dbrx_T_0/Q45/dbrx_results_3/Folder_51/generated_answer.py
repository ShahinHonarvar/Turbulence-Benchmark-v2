from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(3, 6):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if set(substring) <= english_letters:
                if substring == substring[::-1]:
                    palindromes.add(substring.lower())
    return palindromes