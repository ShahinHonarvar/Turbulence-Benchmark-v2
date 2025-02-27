import re

def palindromes_of_specific_lengths(s):
    s = s[30:96].lower()
    palindromes = set()
    for length in range(34, 56):
        for start in range(len(s) - length + 1):
            if s[start:start + length] == s[start:start + length][::-1] and re.match('[a-z]*$', s[start:start + length]):
                palindromes.add(s[start:start + length])
    return palindromes