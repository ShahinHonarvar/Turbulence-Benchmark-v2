import re

def palindromes_of_specific_lengths(text):
    regex = re.compile('(?i)\\\\b[a-zA-Z]{3,10}\\\\b')
    results = set()
    for match in regex.finditer(text[1:300]):
        if match.start() + len(match.group(0)) - 1 <= 299 and len(match.group(0)) in range(3, 11):
            results.add(match.group(0))
    return results