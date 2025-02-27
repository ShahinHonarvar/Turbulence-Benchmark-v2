import re

def palindrome_of_length_n(s):
    s = s.lower()
    return set(re.findall('\\b\\w{7}\\b', s)) & set((i for i in [s[i:i + 7] for i in range(len(s) - 6)] if i == i[::-1] and i.isalpha()))