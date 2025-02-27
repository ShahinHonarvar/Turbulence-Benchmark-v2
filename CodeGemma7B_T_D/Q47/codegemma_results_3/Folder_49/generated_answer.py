import re

def palindromes_of_specific_lengths(text):
    matched = re.findall('(?i)(^[^a-z0-9]{10,50}[^a-z0-9]*?<.*?>.*?)(.*)(\\\\1)', text[10:100])
    if matched:
        return set((palindrome.upper() for palindrome in matched))
    else:
        return set()