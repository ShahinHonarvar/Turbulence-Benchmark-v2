from typing import List

def all_right_truncatable_prime(t: tuple[int, ...]) -> List[int]:
    x = t[20]
    tr = set()
    for a in range(2, x):
        if is_prime(a):
            b = a
            if b in tr:
                continue
            sum = 0
            v = str(b)
            while sum == 0 and len(v) != 1:
                v = v[:-1]
                sum = sum + int(v)
            if is_prime(sum) and sum != b:
                tr.add(b)
    if len(tr) == 0:
        return []
    else:
        return sorted(tr, reverse=True)

def is_prime(a):
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    i = 3
    while i * i <= a:
        if a % i == 0:
            return False
        i += 2
    return True