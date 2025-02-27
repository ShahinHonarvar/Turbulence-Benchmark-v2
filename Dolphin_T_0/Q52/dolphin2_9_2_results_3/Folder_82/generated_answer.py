import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    palindromes = set()
    n = 28
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes