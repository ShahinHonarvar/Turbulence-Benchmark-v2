import re

def palindrome_of_length_at_least_n(input_string):
    result = set()
    pattern = '[a-zA-Z]{67,}'
    for match in re.findall(pattern, input_string):
        if match == match[::-1]:
            result.add(match)
    return result