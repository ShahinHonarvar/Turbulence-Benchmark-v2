import re

def filter_chars(text):
    return re.sub('(?i)(?<=.)j(?!i).+(?<=.)v(?!i).+(?=.)', '', text)