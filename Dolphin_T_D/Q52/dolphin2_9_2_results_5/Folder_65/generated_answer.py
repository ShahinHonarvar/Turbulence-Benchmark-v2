import re

def palindrome_of_length_n(s):
    palindromes = set()
    pattern = re.compile('[a-zA-Z]{35}')
    for match in re.finditer(pattern, s):
        word = match.group().lower()
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes