import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    palindrome_set = set()
    for i in range(len(s) - 15):
        substring = s[i:i + 16]
        if substring == substring[::-1]:
            palindrome_set.add(substring)
    return palindrome_set