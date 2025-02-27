import re

def palindrome_of_length_n(string):
    string = string.lower()
    substrings = set()
    for i in range(len(string) - 50):
        substrings.add(string[i:i + 51])
    return {sub for sub in substrings if sub == sub[::-1] and re.match('^[a-z]+$', sub)}