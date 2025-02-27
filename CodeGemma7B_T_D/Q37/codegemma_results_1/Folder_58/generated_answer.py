import re

def filter_chars(text):
    return re.sub('(?<![^0-9w])[9-w](?![^0-9w])', '', text)