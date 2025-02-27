def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x_tuple):
    x = x_tuple[0]
    primes = []
    for n in range(x, 1, -1):
        str_n = str(n)
        if '0' in str_n:
            continue
        while len(str_n) > 1 and is_prime(int(str_n)):
            str_n = str_n[1:-1]
        if len(str_n) == 2 and is_prime(int(str_n)):
            primes.append(n)
    return sorted(primes, reverse=True)