import re

def all_left_right_truncatable_prime(n):
    s = str(n)
    r = re.sub('0+$', '', s)
    r = re.sub('0+', '', r)
    r = re.sub('2+$', '', r)
    r = re.sub('2+', '', r)
    return sorted(list(set((str(p) for p in range(2, int(s) + 1) if all((p % d for d in range(3, int(s) + 1) if p % d == 0))))))