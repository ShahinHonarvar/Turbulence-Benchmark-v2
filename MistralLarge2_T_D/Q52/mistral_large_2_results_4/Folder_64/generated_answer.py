import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s).lower()
    n = 9
    palindromes = set()
    length = len(s)
    for i in range(length - n + 1):
        substr = s[i:i + n]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes