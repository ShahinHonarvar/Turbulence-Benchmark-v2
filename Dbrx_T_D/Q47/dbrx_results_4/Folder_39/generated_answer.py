import re

def palindromes_of_specific_lengths(s):
    s = s[31:92].lower()
    palindromes = {word for length in range(50, 54) for word in re.findall(f'(?={s})[a-z]{{{length}}}', s)}
    return palindromes or set()