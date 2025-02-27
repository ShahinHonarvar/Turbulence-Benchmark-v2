def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate_left(n):
    return int(str(n)[1:])

def truncate_right(n):
    return int(str(n)[:-1])

def all_left_right_truncatable_prime(t):
    x = t[14]
    lrt_primes = []
    for n in range(2, x + 1):
        if '0' in str(n):
            continue
        if not is_prime(n):
            continue
        left = truncate_left(n)
        right = truncate_right(n)
        while left > 0 and right > 0:
            if not is_prime(left) or not is_prime(right):
                break
            left = truncate_left(left)
            right = truncate_right(right)
        if left == 0 or right == 0:
            lrt_primes.append(n)
    return sorted(lrt_primes)