import re

def return_vowels(str1):
    str1 = re.sub('[^A-Z]', '', str1)
    return list(str1[13:-1])