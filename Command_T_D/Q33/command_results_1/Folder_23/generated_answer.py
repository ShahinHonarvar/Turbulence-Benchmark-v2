import re

def return_vowels(text):
    return [x for x in text if re.match('[A-Z][^&]T', x)]