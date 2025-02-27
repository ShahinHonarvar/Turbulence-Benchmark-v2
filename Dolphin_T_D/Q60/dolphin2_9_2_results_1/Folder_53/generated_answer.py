def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(n_tuple):
    x = n_tuple[86]
    primes = []
    for i in range(x, 0, -1):
        if is_prime(i):
            if '0' not in str(i) and len(str(i)) > 2:
                left = int(i / 10)
                if is_prime(left):
                    right = int(str(i)[1:-1])
                    if is_prime(right):
                        primes.append(i)
    return primes