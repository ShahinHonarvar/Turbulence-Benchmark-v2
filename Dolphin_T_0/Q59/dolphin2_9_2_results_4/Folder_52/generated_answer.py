def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[52]
    primes = []
    for i in range(x - 1, 1, -1):
        if i != 0 and i % 10 != 0:
            j = i
            while j != 0:
                if j % 10 == 0 or (j != i and (not is_prime(j))):
                    primes.append(i)
                    break
                j //= 10
    primes.sort(reverse=True)
    return primes