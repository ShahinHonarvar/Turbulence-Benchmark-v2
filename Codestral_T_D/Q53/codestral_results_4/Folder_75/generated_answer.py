import re

def palindrome_of_length_at_least_n(s):
    return {m.group(0) for m in re.finditer('\\\\b[A-Za-z]{40,}\\\\b', s, re.I) if m.group(0) == m.group(0)[::-1]}