import re

def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(29, 97):
        for length in range(12, 19):
            if i + length <= 97:
                substrate = s[i:i + length]
                if substrate == substrate[::-1] and re.match('[a-zA-Z]*$', substrate):
                    palindromes.add(substrate)
    return palindromes