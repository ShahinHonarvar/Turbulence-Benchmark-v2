import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    pattern = re.compile('(?i)(\\\\b\\\\w{40,72}\\\\b)', re.MULTILINE)
    matches = pattern.findall(text[15:89])
    return set(filter('\\\\b[a-zA-Z]+\\\\b'.match, matches))