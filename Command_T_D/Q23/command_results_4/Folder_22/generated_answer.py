import re

def find_divisors_in_range(n):
    s = str(n)
    divs = set(re.findall('(\\d+)', s))
    return [int(d) for d in divs if d >= 4 and d <= 7]