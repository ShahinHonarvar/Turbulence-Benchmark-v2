def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[433]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    lrt_primes = []
    for p in primes:
        if '0' not in str(p):
            truncated = True
            n = p
            while n > 0:
                n = int(str(n)[1:])
                if not is_prime(n) and n != 0:
                    truncated = False
                    break
            n = p
            while n > 0:
                n = int(str(n)[:-1])
                if not is_prime(n) and n != 0:
                    truncated = False
                    break
            if truncated:
                lrt_primes.append(p)
    return sorted(lrt_primes, reverse=True)