import re

def return_vowels(string):
    res = re.findall('<(e|i|o)', string)[0]
    return res