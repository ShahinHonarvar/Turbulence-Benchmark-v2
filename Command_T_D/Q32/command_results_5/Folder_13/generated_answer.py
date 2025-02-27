import re

def insert_after_character(str1):
    return re.sub('(x)', '(xN)', str1)