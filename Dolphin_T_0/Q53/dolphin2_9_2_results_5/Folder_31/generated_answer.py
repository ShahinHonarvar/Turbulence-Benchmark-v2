import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 33, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes