import re

def return_vowels(string):
    string = re.sub('[aieou]', '', string)
    return list(string[3:-1])