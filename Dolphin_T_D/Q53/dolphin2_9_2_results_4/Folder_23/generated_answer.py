import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[^a-zA-Z]', '', s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 18, len(s) + 1):
            substring = s[i:j].lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes