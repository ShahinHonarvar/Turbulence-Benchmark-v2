import re

def return_vowels(text):
    result = re.findall('[aeiou][a-w]', text)
    return result