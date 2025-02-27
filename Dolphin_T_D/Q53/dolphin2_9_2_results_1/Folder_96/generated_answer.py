import re

def palindrome_of_length_at_least_n(s):
    palindrome_set = set()
    s = s.lower()
    for i in range(len(s) - 23):
        substring = s[i:i + 24]
        substrings = re.findall('[a-zA-Z]+', substring)
        for substring in substrings:
            if len(substring) >= 24 and substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set