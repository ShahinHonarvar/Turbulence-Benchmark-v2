import re

def return_vowels(s):
    for m in re.finditer('<(.)>{23}(?<=.)<(d)', s):
        yield m.group(1)