import re

def palindrome_of_length_n(word):
    patt = re.compile('(?i)\\\\b(\\\\w{147})\\\\b')
    return set(patt.findall(word))