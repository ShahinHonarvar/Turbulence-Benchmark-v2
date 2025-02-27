import re

def palindromes_of_specific_lengths(string):
    lowercased_string = string.lower()
    pattern = re.compile('(?i)(?<![a-z])[a-z]{26,33}(?![a-z])')
    matches = pattern.finditer(lowercased_string)
    filtered_matches = [match.group() for match in matches if 65 <= match.span()[0] <= 99]
    return set(filtered_matches)