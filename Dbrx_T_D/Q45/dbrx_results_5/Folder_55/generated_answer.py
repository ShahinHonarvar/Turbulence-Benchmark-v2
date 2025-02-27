from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(3):
        for j in range(i, 3):
            letters = s[i:j + 1]
            if set(letters).issubset(english_letters):
                palindromes.add(''.join(sorted(letters)).lower())
    for i in range(3, len(s)):
        for j in range(i, len(s)):
            for k in range(i, j + 1):
                letters = s[i:j + 1]
                if s[k] in english_letters:
                    palindromes.add(''.join(sorted(letters)[:k - i + 1] + [s[k]] + sorted(letters)[k - i + 1:]).lower())
    return {palindrome for palindrome in palindromes if len(palindrome) >= 3}