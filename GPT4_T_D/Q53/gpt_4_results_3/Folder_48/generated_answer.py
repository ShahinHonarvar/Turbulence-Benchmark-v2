import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[^a-z]', '', s.lower())
    len_s = len(s)
    palindromes = set()
    for i in range(len_s):
        for j in range(i + 150, len_s + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes