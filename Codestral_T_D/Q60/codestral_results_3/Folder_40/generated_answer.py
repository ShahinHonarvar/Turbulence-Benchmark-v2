def all_left_right_truncatable_prime(t):
    x = t[10]
    primes = []
    for num in range(2, x + 1):
        if all((is_prime(int(str(num)[:i])) and is_prime(int(str(num)[i:])) for i in range(1, len(str(num))))):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True