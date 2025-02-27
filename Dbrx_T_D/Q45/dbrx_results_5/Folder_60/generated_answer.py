from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s = s[3:6 + 1]
    s = ''.join((c.lower() for c in s if c.lower() in english_letters))
    if len(s) < 4 or s[0] != s[-1]:
        return set()
    palindromes = set()
    for i in range(len(s) - 1):
        for j in range(i, len(s)):
            palindrome = s[i:j + 1]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes