import re

def palindromes_of_specific_lengths(input_string):
    input_string = input_string.lower()
    substring = input_string[200:301]
    palindromes = set()
    for length in range(10, 51):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if re.fullmatch('[a-z]*', candidate):
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes