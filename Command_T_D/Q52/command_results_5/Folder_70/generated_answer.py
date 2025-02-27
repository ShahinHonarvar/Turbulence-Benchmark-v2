import re

def palindrome_of_length_n(string):
    pal = set()
    for m in re.finditer('([a-z]+)(?=\\W\\1)', string.lower()):
        pal.add(m.group(1))
    return pal