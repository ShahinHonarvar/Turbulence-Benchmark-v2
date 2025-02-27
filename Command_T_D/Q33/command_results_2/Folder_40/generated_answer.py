import re

def return_vowels(string):
    return re.findall('([^aieou])([aieou])([^aieou]?)', string)