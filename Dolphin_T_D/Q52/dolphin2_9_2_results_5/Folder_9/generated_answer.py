import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 71):
        sub = s[i:i + 72]
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes