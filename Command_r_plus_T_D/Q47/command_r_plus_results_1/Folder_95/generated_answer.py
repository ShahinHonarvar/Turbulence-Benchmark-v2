import re

def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[11:57]
    pattern = re.compile('[a-zA-Z]{20,21}')
    matches = pattern.finditer(substring)
    for match in matches:
        word = match.group()
        if word.lower() == word[::-1].lower():
            palindromes.add(word)
    return palindromes