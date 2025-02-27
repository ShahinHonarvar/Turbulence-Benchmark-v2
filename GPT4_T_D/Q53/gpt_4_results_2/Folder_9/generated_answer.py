import re

def palindrome_of_length_at_least_n(s):
    s = re.findall('\x08\\w+\x08', s)
    palindrome_set = set()
    for word in s:
        word = word.lower()
        if len(word) >= 95 and word == word[::-1]:
            palindrome_set.add(word)
    return palindrome_set