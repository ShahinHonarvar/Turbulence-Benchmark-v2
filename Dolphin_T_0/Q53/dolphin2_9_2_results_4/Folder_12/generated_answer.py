import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[^a-z]', '', s.lower())
    n = 51
    palindromes = set()
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes