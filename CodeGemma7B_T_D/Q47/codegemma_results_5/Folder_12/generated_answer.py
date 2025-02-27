import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    regex = '(?<=^.{62})(.{18,21})(?=.{89})'
    matches = re.findall(regex, text)
    palindromes = set([word for word in matches if word == word[::-1]])
    return palindromes