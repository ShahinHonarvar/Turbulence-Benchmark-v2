import re

def return_vowels(s):
    return re.findall('([eio][^aieuf])', s)[1:-1]