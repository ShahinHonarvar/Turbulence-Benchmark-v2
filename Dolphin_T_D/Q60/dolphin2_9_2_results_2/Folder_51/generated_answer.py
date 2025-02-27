def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):

    def is_left_right_truncatable(n):
        n = str(n)
        while len(n) > 1:
            n = n[1:-1]
            if len(n) > 0 and (not is_prime(int(n))):
                return False
        return True
    x = t[54]
    primes = []
    for i in range(2, x + 1):
        if is_prime(i) and is_left_right_truncatable(i):
            primes.append(i)
    return sorted(primes)