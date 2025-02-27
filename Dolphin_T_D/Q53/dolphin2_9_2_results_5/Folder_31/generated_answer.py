import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    regex = re.compile('(?=(\\w\\w\\w\\w\\w\\w\\w\\w\\w\\w\\w\\w\\w\\w\\w\\w\\w\\w\\w\\w\\w\\w\\w\\w\\w\\w\\w))')
    matches = set(regex.findall(s))
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes