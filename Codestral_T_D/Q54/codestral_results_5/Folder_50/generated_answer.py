def all_right_truncatable_prime(numbers):
    x = numbers[57]
    trunc_primes = []
    for i in range(2, x):
        if all((is_prime(int(str(i)[:j])) for j in range(1, len(str(i)) + 1))):
            trunc_primes.append(i)
    return sorted(trunc_primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(n ** 0.5) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True