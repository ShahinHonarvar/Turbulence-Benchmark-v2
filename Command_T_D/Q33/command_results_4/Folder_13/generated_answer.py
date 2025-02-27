import re

def return_vowels(s):
    s = re.sub('[^aieouAEIOU]', '', s)
    return s[149:313]