import re

def palindrome_of_length_at_least_n(input_str):
    patterns = [''.join(reversed(w)) for w in re.findall('\\b\\w+\\b', input_str.lower())]
    return set((w for w in patterns if len(w) >= 95))