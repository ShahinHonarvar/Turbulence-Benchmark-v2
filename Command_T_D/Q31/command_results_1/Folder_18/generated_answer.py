import re

def if_perfect_num(a):
    return bool(re.match('(\\d+)(?=\\D\\1)', str(a[312])))