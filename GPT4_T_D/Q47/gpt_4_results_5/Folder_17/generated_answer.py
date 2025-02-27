import re

def palindromes_of_specific_lengths(string):
    string = string[22:96].lower()
    palindromes = set()
    for length in range(52, 56):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring == substring[::-1] and re.match('^[a-z]*$', substring):
                palindromes.add(substring)
    return palindromes