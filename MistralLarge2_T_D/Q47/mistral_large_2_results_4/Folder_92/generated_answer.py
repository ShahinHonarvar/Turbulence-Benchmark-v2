import re

def palindromes_of_specific_lengths(s):
    substring = s[:5].lower()
    palindromes = set()
    for i in range(len(substring)):
        for length in range(3, 5):
            if i + length <= len(substring):
                candidate = substring[i:i + length]
                if candidate == candidate[::-1] and re.match('^[a-z]+$', candidate):
                    palindromes.add(candidate)
    return palindromes