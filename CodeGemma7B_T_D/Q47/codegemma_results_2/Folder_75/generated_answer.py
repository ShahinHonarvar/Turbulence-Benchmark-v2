import re

def palindromes_of_specific_lengths(text):
    pattern = re.compile('[A-Za-z]{23,39}', re.IGNORECASE)
    palindromes = set()
    for i in range(31, 75):
        substr = text[i:i + 1 + i - 31]
        for palindrome in re.findall(pattern, substr):
            palindromes.add(palindrome)
    return palindromes