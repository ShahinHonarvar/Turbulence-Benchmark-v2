import re

def palindromes_of_specific_lengths(string):
    string = string[13:100]
    palindromes = set()
    for length in range(26, 30):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring.lower() == substring.lower()[::-1] and re.match('^[a-zA-Z]*$', substring):
                palindromes.add(substring)
    return palindromes