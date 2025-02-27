import re

def return_vowels(str1):
    str1 = re.sub('[^A-Z0-9]', '', str1)
    str1 = str1[11:61]
    str1 = re.sub('[^A-Z]', '', str1)
    return list(str1)