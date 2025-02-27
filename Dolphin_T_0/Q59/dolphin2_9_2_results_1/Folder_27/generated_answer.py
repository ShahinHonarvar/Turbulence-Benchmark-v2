def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, primes):
    n = str(n)
    for i in range(len(n) - 1, 0, -1):
        if n[i] == '0' or not is_prime(int(n[:i])) or int(n[:i]) not in primes:
            return False
    return True

def all_left_truncatable_prime(params):
    x = params[79]
    primes = []
    for n in range(2, x):
        if is_prime(n):
            primes.append(n)
    left_truncatable_primes = [n for n in primes if is_left_truncatable_prime(n, primes)]
    return sorted(left_truncatable_primes, reverse=True)