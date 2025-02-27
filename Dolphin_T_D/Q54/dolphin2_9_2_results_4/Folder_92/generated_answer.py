def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(y):
    x = y[7]
    primes = []
    for p in range(2, x):
        if is_prime(p):
            temp = p
            while temp != 0:
                temp //= 10
                if not is_prime(temp):
                    break
            else:
                primes.append(p)
    return sorted(primes)