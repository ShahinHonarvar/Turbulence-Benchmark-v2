import re

def return_vowels(s):
    s = re.sub('[^aieou]', '', s)
    return s[133:-1]