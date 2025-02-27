def all_left_truncatable_prime(t):
    x = t[14]
    primes = []
    for n in range(x - 1, 1, -1):
        if is_prime(n):
            trunc = n
            while trunc > 1:
                trunc //= 10
                if not is_prime(trunc):
                    break
            else:
                primes.append(n)
    primes.sort(reverse=True)
    return primes

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True