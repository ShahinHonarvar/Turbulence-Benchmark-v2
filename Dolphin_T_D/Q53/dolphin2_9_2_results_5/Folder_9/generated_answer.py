import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = re.sub('[^a-zA-Z]', '', s)
    for i in range(len(s)):
        for j in range(i + 8, len(s)):
            if s[i:j + 1].lower() == s[i:j + 1].lower()[::-1] and j - i + 1 >= 95:
                palindromes.add(s[i:j + 1])
    return palindromes