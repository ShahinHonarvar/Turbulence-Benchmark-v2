def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[88]
    primes = [a for a in range(x, 1, -1) if is_prime(a)]
    return sorted([a for a in primes if all((int(''.join(filter(str.isdigit, str(a)[i:])) if i > 0 else a) in primes for i in range(len(str(a)))))], reverse=True)