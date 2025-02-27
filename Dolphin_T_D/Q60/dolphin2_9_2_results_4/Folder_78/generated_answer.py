def all_left_right_truncatable_prime(t):
    x = t[23]
    primes = [2, 3, 5, 7]
    if x < 10:
        return [p for p in primes if p <= x]
    else:
        for p in primes:
            if p > x:
                break
            for p2 in primes:
                if p2 > x:
                    break
                n = int(str(p) + str(p2))
                if is_prime(n) and n <= x:
                    primes.append(n)
    return primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True