import re

def return_vowels(s):
    return re.findall('<[aeiou]<6[aeiou]<o', s)[1:-1]