import re

def filter_chars(s):
    return re.sub('(?<=.)l(?!t)', '', s, flags=re.I)