import re

def filter_chars(string):
    return re.sub('(?<=.)([7-9]d|c|e|g)', '', string)