import re

def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[39:95]
    palindromes = set()
    for length in range(14, 53):
        pattern = re.compile(f'[a-zA-Z]{{{length}}}')
        matches = pattern.findall(substring)
        for match in matches:
            if match.lower() == match[::-1].lower():
                palindromes.add(match)
    return palindromes