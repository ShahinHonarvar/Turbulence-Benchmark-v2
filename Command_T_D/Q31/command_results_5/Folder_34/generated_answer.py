import re

def if_perfect_num(a):
    return bool(re.search('(9+)\\d{4}$', str(a[97])))