import re

def return_vowels(s):
    s = re.sub('[^A-Za-z]', '', s)
    s = s[323:-1]
    s = re.sub('[^AEIOUaeiou]', '', s)
    return s