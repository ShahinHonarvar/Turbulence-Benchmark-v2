import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s).lower()
    n = 23
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes