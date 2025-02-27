import re

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    pattern = re.compile('(?=(.[\\\\1-z]{53,}))[\\\\1-z]{54,}', re.I | re.U)
    return set(pattern.findall(text))