import re

def palindromes_of_specific_lengths(string):
    substr = string[29:99]
    palindromes = set()
    for i in range(6, 10):
        for j in range(len(substr) - i + 1):
            s = substr[j:j + i]
            if re.match('^[A-Za-z]*$', s) and s.lower() == s[::-1].lower():
                palindromes.add(s)
    return palindromes