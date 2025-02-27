import re

def palindromes_of_specific_lengths(text):
    regex = re.compile('(?i)^.{12,122}[A-Za-z]{12,220}[A-Za-z].*$')
    palindromes = set()
    for word in text.split():
        if regex.match(word):
            word = word.lower()
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes