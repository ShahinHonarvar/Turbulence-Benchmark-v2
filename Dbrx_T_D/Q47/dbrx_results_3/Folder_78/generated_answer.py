import re

def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    for i in range(15, 73):
        for j in range(19, 56):
            substring = input_string[i:i + j].lower()
            if substring == substring[::-1] and re.fullmatch('[a-zA-Z]*', substring):
                palindromes.add(substring)
    return palindromes