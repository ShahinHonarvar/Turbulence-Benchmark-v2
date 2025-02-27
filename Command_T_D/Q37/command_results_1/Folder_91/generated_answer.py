import re

def filter_chars(s):
    return re.sub('((?<=A)[B-H](?=C))', '', s)