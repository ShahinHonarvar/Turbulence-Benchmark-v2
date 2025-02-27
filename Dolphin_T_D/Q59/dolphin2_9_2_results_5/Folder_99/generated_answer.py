def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[757]
    left_truncatable_primes = []
    for i in range(2, x):
        j = i
        while j:
            if j == 0:
                left_truncatable_primes.append(i)
                break
            if not is_prime(j):
                break
            j //= 10
    return sorted(left_truncatable_primes)