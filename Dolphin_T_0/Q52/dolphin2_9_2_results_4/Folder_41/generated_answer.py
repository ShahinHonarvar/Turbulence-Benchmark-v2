import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 59):
        candidate = s[i:i + 60]
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes