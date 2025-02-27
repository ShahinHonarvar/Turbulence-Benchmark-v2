import re

def filter_chars(str):
    return re.sub('(?!<\\s).(?!<\\s).(?!<\\s).(?!<\\s).(?!<\\s).(?!<\\s).(?!<\\s)', '', str)