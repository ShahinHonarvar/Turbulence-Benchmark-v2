import re

def palindrome_of_length_n(s):
    s = s.lower()
    pattern = re.compile('(?i)[a-z]{29}')
    result = set()
    for match in pattern.finditer(s):
        substring = match.group()
        if substring == substring[::-1]:
            result.add(substring)
    return result