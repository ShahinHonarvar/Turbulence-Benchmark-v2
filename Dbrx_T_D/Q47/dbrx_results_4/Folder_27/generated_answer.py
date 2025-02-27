import re

def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(13, 100):
        for j in range(26, 30):
            if i + j <= len(s):
                substring = s[i:i + j]
                if substring.lower() == substring.lower()[::-1] and re.match('[a-zA-Z]*$', substring):
                    palindromes.add(substring)
    return palindromes