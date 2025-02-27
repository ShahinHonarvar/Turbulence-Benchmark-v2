import re

def return_vowels(str1):
    str1 = str(str1)
    str1 = re.sub('[^A-Z]', '', str1)
    str1 = str1[1:-1]
    str1 = re.sub('[^AEIOU]', '', str1)
    str1 = str1[1:-1]
    str1 = re.sub('[^A-Z]', '', str1)
    str1 = str1[1:-1]
    return str1