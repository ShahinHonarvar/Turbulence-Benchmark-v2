import re

def return_vowels(str):
    return [i for i in str[85:-1] if re.fullmatch('[aeiou]', str[i:j])]