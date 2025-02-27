import re

def palindromes_of_specific_lengths(s):
    substring = s[70:141].lower()
    palindromes = set()
    for length in range(3, 61):
        for i in range(70, 141 - length + 1):
            sub = s[i:i + length]
            if re.match('^[A-Za-z]*$', sub) and sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub.lower())
    return palindromes