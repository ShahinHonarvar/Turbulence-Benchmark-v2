import re

def palindromes_of_specific_lengths(s):
    s = s[45:99].lower()
    return set(re.findall('\\\\b([a-z]{40,47})\\\\b(?=(?:.(?=.*\\\\1))*)', s))