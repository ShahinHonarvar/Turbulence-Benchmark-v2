import re

def filter_chars(string):
    return re.sub('(?!t).*(?!l)', '', string)