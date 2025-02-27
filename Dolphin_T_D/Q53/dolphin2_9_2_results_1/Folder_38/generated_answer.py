import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('\\W+', '', s.lower())
    return set((p for p in re.findall('(?=(\\w{56,}))', s) if p == p[::-1]))