import re

def palindromes_of_specific_lengths(text):
    pattern = re.compile('(?i)([a-zA-Z]{38,60})')
    palindromes = set()
    for i in range(18, 88):
        substring = text[i:i + 61]
        for match in pattern.finditer(substring):
            palindrome = match.group(1)
            palindromes.add(palindrome)
    return palindromes