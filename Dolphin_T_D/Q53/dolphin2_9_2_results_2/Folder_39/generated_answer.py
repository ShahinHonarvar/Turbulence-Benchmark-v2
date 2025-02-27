import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    result = set()
    for i in range(69, len(string) + 1):
        for j in range(len(string) - i + 1):
            substring = string[j:j + i]
            if re.match('^[a-z]*$', substring) and substring == substring[::-1]:
                result.add(substring)
    return result