import re

def filter_chars(str):
    return re.sub('(?!<=20)(?<=25)', '', str)