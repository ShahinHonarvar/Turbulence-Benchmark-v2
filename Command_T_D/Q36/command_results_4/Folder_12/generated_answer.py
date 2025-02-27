import re

def filter_chars(string):
    return re.sub('<[a-z]+>', '', string)