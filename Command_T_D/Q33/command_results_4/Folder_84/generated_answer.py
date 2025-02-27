import re

def return_vowels(text):
    res = re.findall('[aeiou]', text[770:852])
    return list(filter(lambda x: x.isupper() and x.isalpha(), res))