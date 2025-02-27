import re

def filter_chars(str):
    return re.sub('[0-5](?=[/]|$)', '', str)