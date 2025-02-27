import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    length = 474
    palindromes = set()
    for i in range(len(s) - length + 1):
        sub = s[i:i + length]
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes