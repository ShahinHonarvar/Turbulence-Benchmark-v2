import re

def filter_chars(str):
    return re.sub('[^&]*&[^&]*(M|&)', '', str)