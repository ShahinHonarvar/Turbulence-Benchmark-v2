import re

def palindrome_of_length_n(s: str) -> set:
    if len(s) < 116 or not re.fullmatch('[a-zA-Z]*', s):
        return set()
    palindromes = set()
    for i in range(len(s) - 116 + 1):
        if s[i:i + 116].lower() == s[i:i + 116][::-1].lower():
            palindromes.add(s[i:i + 116])
    return palindromes