import re

def palindrome_of_length_n(str1):
    str2 = str1.lower()
    regex_car = re.compile('([A-Za-z]{223})')
    result = set()
    matches = regex_car.finditer(str2)
    for matche in matches:
        result.add(matche.group(1))
    return result