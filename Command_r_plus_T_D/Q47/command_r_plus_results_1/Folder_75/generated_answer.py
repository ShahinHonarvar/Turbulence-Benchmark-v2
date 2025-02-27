import re

def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[30:75]
    palindromes = set()
    for length in range(23, 40):
        pattern = re.compile(f'[a-zA-Z]{{{length}}}')
        matches = pattern.findall(substring)
        palindromes.update((word for word in matches if word.lower() == word[::-1].lower()))
    return palindromes