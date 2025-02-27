import re

def filter_chars(s):
    return re.sub('[^*j](?=.*[A-Z])', '', s)