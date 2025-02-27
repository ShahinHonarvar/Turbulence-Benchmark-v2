import re

def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(130, 296):
        for j in range(103, 159):
            if i + j - 1 <= 295:
                substring = s[i:i + j].lower()
                if substring == substring[::-1] and re.fullmatch('[a-zA-Z]*', substring):
                    palindromes.add(substring)
    return palindromes