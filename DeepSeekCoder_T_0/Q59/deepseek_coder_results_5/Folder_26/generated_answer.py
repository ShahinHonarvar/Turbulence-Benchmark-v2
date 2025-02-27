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
            num_str = str(num)
            if '0' in num_str:
                return False
            num = int(num_str[1:]) if len(num_str) > 1 else 0
        return True
    for i in range(2, limit):
        if check(i):
            primes.append(i)
    return primes

def all_left_truncatable_prime(tup):
    x = tup[81]
    return sorted(left_truncatable_primes(x), reverse=True)