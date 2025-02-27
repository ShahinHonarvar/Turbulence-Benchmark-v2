import re

def insert_at_index(lst):
    return re.sub('(?<=\\d)\\d\\.(?=\\d)', '11.04', lst)