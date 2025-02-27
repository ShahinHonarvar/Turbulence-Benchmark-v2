import re

def insert_after_index(lst):
    return re.sub('(\\d+)$', '\\1,72.27', lst)