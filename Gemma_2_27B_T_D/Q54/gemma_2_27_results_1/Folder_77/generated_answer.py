def all_right_truncatable_prime(t):
    x = t[767]
    primes = []
    for num in range(x, 0, -1):
        if is_prime(num):
            is_truncatable = True
            n = str(num)
            while len(n) > 0:
                if not is_prime(int(n)):
                    is_truncatable = False
                    break
                n = n[:-1]
            if is_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True