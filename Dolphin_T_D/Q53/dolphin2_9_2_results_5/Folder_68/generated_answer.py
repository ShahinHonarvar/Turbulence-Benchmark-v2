import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 21, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes