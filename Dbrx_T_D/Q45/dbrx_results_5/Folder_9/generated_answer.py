from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letters = {l for l in s[0:7] if l in english_letters}
    if len(letters) < 7:
        return set()
    palindromes = set()
    for i in range(6, len(s)):
        for j in range(i - 6, 0, -1):
            if s[i] in letters and s[j] in letters:
                palindrome = s[j:i + 1]
                if is_palindrome(palindrome):
                    palindromes.add(palindrome.lower())
    return palindromes

def is_palindrome(s):
    return s == s[::-1]