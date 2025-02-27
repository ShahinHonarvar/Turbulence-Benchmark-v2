import re

def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text)):
        for j in range(i, len(text)):
            substring = text[i:j + 1]
            if len(substring) >= 20 and substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result