import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[23:95]
    for j in range(17, 56):
        for i in range(len(substring) - j + 1):
            potential = substring[i:i + j]
            if potential.lower() == potential.lower()[::-1] and potential.isalpha():
                palindromes.add(potential)
    return palindromes