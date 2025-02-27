import re

def palindrome_of_length_n(input_string):
    input_string = re.sub('\\W+', '', input_string.lower())
    n = 472
    result = set()
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if substring == substring[::-1]:
            result.add(substring)
    return result