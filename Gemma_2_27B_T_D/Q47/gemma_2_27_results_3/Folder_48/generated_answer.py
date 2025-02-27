import re

def palindromes_of_specific_lengths(text):
    return set((match.group(0) for match in re.finditer('[a-zA-Z]{104,120}', text[155:284], re.IGNORECASE) if match.group(0) == match.group(0)[::-1]))