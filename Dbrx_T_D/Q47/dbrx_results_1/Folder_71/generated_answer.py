import re

def palindromes_of_specific_lengths(input_string):
    input_string = input_string[18:66]
    palindromes = set()
    for i in range(23, 37):
        for j in range(len(input_string) - i + 1):
            if re.fullmatch('[a-zA-Z]*', input_string[j:j + i]) and input_string[j:j + i].lower() == input_string[j:j + i][::-1].lower():
                palindromes.add(input_string[j:j + i])
    return palindromes