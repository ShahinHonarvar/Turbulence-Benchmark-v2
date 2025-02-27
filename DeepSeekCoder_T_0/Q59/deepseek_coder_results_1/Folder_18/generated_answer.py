def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(limit):
    primes = []

    def check(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = int(str(n)[1:]) if str(n)[1:] else 0
        return True
    for num in range(2, limit):
        if '0' not in str(num) and check(num):
            primes.append(num)
    return primes

def all_left_truncatable_prime(tup):
    x = tup[429]
    return sorted(left_truncatable_primes(x), reverse=True)