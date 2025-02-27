import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    pals = set()
    for i in range(len(s) - 444):
        subs = s[i:i + 445]
        if subs == subs[::-1]:
            pals.add(subs)
    return pals