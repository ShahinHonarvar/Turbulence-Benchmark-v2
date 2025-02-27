import re

def filter_chars(string):
    return re.sub('([%u343-665])', '', string)