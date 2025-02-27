import re

def palindrome_of_length_n(s):
    s = re.sub('[^A-Za-z]', '', s)
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 12):
        if s[i:i + 13] == s[i:i + 13][::-1]:
            palindromes.add(s[i:i + 13])
    return palindromes