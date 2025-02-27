import re

def palindrome_of_length_n(str):
    result = set()
    for i in range(len(str) - 45):
        for j in range(i + 1, len(str) - 44):
            if re.match('^[A-Za-z]*$', str[i:j + 1]):
                result.add(str[i:j + 1])
    return result