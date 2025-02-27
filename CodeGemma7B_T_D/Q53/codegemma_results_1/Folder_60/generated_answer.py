import re

def palindrome_of_length_at_least_n(s):
    result = set()
    regex = re.compile('[a-zA-Z]{80,}')
    for match in regex.finditer(s):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            result.add(palindrome)
    if not result:
        return set()
    else:
        return result