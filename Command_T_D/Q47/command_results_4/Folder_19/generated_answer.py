import re

def palindromes_of_specific_lengths(s):
    matches = re.finditer('(?i)(?<=\\d{10})[a-z]{3}(?<=\\d{55})[a-z]{3}\\1', s)
    return set((m.group() for m in matches if m.group() == m.group(0)[::-1]))