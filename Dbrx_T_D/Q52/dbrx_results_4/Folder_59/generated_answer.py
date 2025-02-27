import re

def palindrome_of_length_n(string):
    letters = re.findall('[a-zA-Z]', string)
    n = 39
    result = set()
    if n > len(letters) or n < 1:
        return result
    for i in range(len(letters) - n + 1):
        if all((letters[i + j] == letters[i + n - j] for j in range(n))):
            result.add(''.join(letters[i:i + n]))
    return result