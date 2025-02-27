import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[^A-Za-z]', '', s)
    palindromes = set()
    for i in range(len(s) - 19):
        subs = s[i:i + 20]
        if subs == subs[::-1]:
            palindromes.add(subs.lower())
    return palindromes