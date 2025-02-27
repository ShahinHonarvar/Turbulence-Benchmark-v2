import re

def palindromes_of_specific_lengths(s: str) -> set:
    s = s.lower()
    palindromes = {s[i:j + 1] for i in range(1, 10) for j in range(i, min(i + 7, 10)) if s[i:j + 1] == s[i:j + 1][::-1] and re.match('[a-zA-Z]', s[i:j + 1])}
    return palindromes if palindromes else {''}