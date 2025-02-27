def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fill_primes(n):
    primes = [2]
    num = 3
    while num <= n:
        if is_prime(num):
            primes.append(num)
        num += 2
    return primes

def all_left_truncatable_prime(t):
    x = t[10]
    primes = fill_primes(x)
    left_truncatable = []
    for p in primes:
        if '0' not in str(p):
            trunc = p
            while trunc > 1:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                left_truncatable.append(p)
    left_truncatable.sort(reverse=True)
    return left_truncatable