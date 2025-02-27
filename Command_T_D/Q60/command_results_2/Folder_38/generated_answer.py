import re

def all_left_right_truncatable_prime(tup):
    x, = tup
    return sorted([n for n in range(2, x + 1) if re.match('(\\d)([23579])(\\d)', str(n))], key=lambda n: n)