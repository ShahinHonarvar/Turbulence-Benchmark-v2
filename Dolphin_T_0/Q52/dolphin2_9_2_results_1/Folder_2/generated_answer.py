import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    length = 147
    palindromes = set()
    for i in range(len(s) - length + 1):
        subs = s[i:i + length]
        if subs == subs[::-1]:
            palindromes.add(subs)
    return palindromes