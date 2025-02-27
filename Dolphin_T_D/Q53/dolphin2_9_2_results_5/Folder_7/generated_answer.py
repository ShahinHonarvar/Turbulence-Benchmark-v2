import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            sub_s = s[i:j]
            if len(sub_s) >= 12 and sub_s == sub_s[::-1]:
                palindromes.add(sub_s)
    return palindromes