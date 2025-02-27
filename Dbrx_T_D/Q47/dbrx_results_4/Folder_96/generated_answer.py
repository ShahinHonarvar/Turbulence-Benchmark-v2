import re

def palindromes_of_specific_lengths(string):
    string = string[100:301]
    palindromes = set()
    for i in range(50, 101):
        for j in range(len(string) - i + 1):
            if re.fullmatch('[a-zA-Z]*', string[j:j + i]) and string[j:j + i].lower() == string[j:j + i][::-1].lower():
                palindromes.add(string[j:j + i])
    return palindromes