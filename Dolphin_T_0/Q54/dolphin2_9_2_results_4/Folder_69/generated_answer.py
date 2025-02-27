def all_right_truncatable_prime(t):
    x = t[760]
    primes = []
    for i in range(x, 0, -1):
        if is_prime(i):
            k = i
            while k > 1:
                k = k // 10
                if not is_prime(k):
                    break
            else:
                primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True