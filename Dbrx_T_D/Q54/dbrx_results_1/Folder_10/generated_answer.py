def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def remove_last_digit(n):
    return int(str(n)[:-1])

def all_right_truncatable_prime(t):
    primes = []
    x = t[38]
    for i in range(2, x):
        if is_prime(i):
            primes.append(i)
    right_truncatable_primes = []
    for prime in primes:
        num = prime
        while num > 1:
            if not is_prime(num):
                break
            right_truncatable_primes.append(num)
            num = remove_last_digit(num)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes