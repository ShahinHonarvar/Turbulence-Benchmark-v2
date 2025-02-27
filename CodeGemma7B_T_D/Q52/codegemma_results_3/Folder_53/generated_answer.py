from typing import Set
from re import finditer

def palindrome_of_length_n(text: str) -> Set[str]:
    letters_regex = '[a-zA-Z]+'
    result = set()
    for match in finditer(letters_regex, text, flags=re.IGNORECASE):
        palindrome = text[match.start():match.end()]
        if len(palindrome) == 68:
            result.add(palindrome)
    return result