import re

def palindrome_of_length_n(s):
    s = re.sub('[^A-Za-z]', '', s)
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 98):
        if s[i:i + 99] == s[i:i + 99][::-1]:
            palindromes.add(s[i:i + 99])
    return palindromes