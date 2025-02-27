import re

def all_right_truncatable_prime(n):
    pattern = re.compile('^[1-9]\\d+$')
    for x in range(2, int(str(n[0]))) + [int(str(n[0]))]:
        if x % 2 == 0 or x % 5 == 0:
            continue
        if pattern.match(str(x)):
            yield x