def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
    return True

def all_left_right_truncatable_prime(lst):
    if isinstance(lst, tuple) and len(lst) > 0:
        x = lst[429]
        primes = [i for i in range(x, -1, -1) if is_prime(i)]
        left_right_truncatable = [i for i in primes if str(i).count('0') == 0 and is_prime(int(str(i)[1:-1]))]
        return sorted(left_right_truncatable, reverse=True)
    return []