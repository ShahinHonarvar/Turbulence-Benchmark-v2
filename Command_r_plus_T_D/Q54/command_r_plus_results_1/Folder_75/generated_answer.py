def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def right_truncatable_primes(num):
    primes = []
    for i in range(10 ** len(str(num)), num, -1):
        if is_prime(i) and all((is_prime(int(str(i)[:j])) for j in range(1, len(str(i))))):
            primes.append(i)
    return primes

def all_right_truncatable_prime(tup):
    x = tup[41]
    primes = right_truncatable_primes(x)
    return sorted(primes)