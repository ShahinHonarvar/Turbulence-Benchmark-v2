def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[36]
    primes = []
    for n in range(x, 1, -1):
        if is_prime(n):
            trunctable = True
            m = n
            while m > 1:
                m //= 10
                if not is_prime(m):
                    trunctable = False
                    break
            if trunctable:
                primes.append(n)
    return primes