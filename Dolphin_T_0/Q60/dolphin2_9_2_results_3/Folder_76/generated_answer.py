import math

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False
    m = int(math.sqrt(n))
    for i in range(3, m + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[370]
    truncatables = []
    for n in range(x, 1, -1):
        if '0' in str(n):
            continue
        trunc = n
        while trunc > 0:
            if not is_prime(trunc):
                break
            trunc = int(str(trunc)[1:-1])
        else:
            truncatables.append(n)
    return sorted(truncatables, reverse=True)