def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(limit):
    primes = []

    def check(num):
        while num > 0:
            if not is_prime(num):
                return False
            num = int(str(num)[1:]) if str(num)[1:] else 0
        return True
    for i in range(2, limit):
        if '0' not in str(i) and check(i):
            primes.append(i)
    return primes

def all_left_truncatable_prime(tup):
    x = tup[760]
    return sorted(left_truncatable_primes(x), reverse=True)