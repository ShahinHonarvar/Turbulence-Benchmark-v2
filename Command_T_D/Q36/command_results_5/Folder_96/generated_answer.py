import re

def filter_chars(string):
    return re.sub('[>._~]{%38,%81}', '', string)