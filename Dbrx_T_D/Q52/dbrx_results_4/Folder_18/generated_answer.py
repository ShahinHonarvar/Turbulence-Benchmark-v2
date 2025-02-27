import re

def palindrome_of_length_n(s: str) -> set[str]:
    s = re.sub('\\W+', '', s).lower()
    result = set()
    for i in range(len(s) - 391):
        substring = s[i:i + 392]
        if substring == substring[::-1]:
            result.add(substring)
    return result