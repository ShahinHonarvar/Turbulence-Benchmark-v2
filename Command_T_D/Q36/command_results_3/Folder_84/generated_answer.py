import re

def filter_chars(s):
    return re.sub('([០-\u17ef]+)', '', s)