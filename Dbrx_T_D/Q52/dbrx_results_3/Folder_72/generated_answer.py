import string

def palindrome_of_length_n(s):
    n = 16
    result = set()
    for i in range(len(s), -1, -1):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if len(substring) < n:
                continue
            if substring.lower() == substring.lower()[::-1] and substring.isalpha() and (len(substring) == n):
                result.add(substring)
    return result