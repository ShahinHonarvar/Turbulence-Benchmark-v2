import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 34):
        for j in range(35):
            if s[i:i + j + 1] == s[i:i + j + 1][::-1] and re.match('[a-zA-Z]+', s[i:i + j + 1]):
                palindromes.add(s[i:i + j + 1])
    return palindromes