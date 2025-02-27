import re

def palindromes_of_specific_lengths(input_string):
    potential_palindromes = set()
    for substring in input_string[125:284]:
        for length in range(109, 127):
            if len(substring) >= length:
                subsubstring = substring[:length]
                if subsubstring.lower() == subsubstring.lower()[::-1] and re.match('[a-zA-Z]*$', subsubstring):
                    potential_palindromes.add(subsubstring)
    return potential_palindromes