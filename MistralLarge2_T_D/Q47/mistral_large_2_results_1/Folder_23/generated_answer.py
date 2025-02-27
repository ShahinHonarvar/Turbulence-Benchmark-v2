import re

def palindromes_of_specific_lengths(s):
    s = s[23:95].lower()
    palindromes = set()
    for length in range(17, 56):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and re.match('^[A-Za-z]*$', substring):
                palindromes.add(substring)
    return palindromes