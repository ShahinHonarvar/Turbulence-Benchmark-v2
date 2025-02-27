from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    start, end = (2, 4)
    if len(s) <= end or not english_letters.intersection(s[start - 1:end + 1]):
        return set()
    string_subset = ''.join((c for c in s[start - 1:end + 1] if c in english_letters))
    if len(string_subset) < 3:
        return set()
    palindromes = set()
    n = len(string_subset)
    for i in range(n - 1):
        for j in range(i + 3, n + 1, 2):
            palindrome = string_subset[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome.lower())
    return palindromes