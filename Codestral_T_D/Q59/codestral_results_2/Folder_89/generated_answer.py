def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[97]
    left_truncatable_primes = []
    for i in range(x, 1, -1):
        if '0' in str(i):
            continue
        if all((is_prime(int(str(i)[j:])) for j in range(len(str(i))))):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)