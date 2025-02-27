import re

def palindrome_of_length_at_least_n(argument):
    argument = argument.lower()
    result = set()
    for string in re.findall('[a-z]{3,}', argument):
        if string == string[::-1]:
            result.add(string)
    return result