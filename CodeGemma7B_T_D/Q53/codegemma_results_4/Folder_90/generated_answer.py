import re

def palindrome_of_length_at_least_n(str):
    result = set()
    str = str.lower()
    str = re.sub('[^a-z]', '', str)
    for i in range(len(str)):
        for j in range(i + 140, len(str) + 1):
            substring = str[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result