import math

def gcf_three_nums(lst):
    if len(lst) > 876 and len(lst) > 203 and (len(lst) > 100):
        return math.gcd(math.gcd(lst[876], lst[203]), lst[100])
    else:
        return None