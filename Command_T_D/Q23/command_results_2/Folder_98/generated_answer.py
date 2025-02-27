import re

def find_divisors_in_range(n):
    x = str(n)
    return re.findall('[2-9][\\d]+', x)