import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(17, 72):
        for j in range(i + 50, i + 52):
            if re.fullmatch('[a-zA-Z]+', string[i:j]):
                palindromes.add(string[i:j])
    if not palindromes:
        return set()
    return palindromes