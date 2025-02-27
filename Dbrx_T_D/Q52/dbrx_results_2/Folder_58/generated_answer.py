from collections import defaultdict

def palindrome_of_length_n(s):
    n = 223
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - n + 1):
        if s[i:i + n] == s[i:i + n][::-1] and all((c.isalpha() for c in s[i:i + n])):
            palindromes.add(s[i:i + n])
    return palindromes