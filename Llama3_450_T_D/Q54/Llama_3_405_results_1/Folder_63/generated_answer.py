def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[88]
    right_truncatable_primes = []
    for i in range(2, x):
        s = str(i)
        if all((is_prime(int(s[:j])) for j in range(len(s), 0, -1))):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)