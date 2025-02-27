import re

def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(49, 52):
        for i in range(27, len(s) - length + 1):
            if s[i:i + length] == ''.join(reversed(s[i:i + length])) and re.match('[a-zA-Z]*$', s[i:i + length]):
                palindromes.add(s[i:i + length])
    return palindromes