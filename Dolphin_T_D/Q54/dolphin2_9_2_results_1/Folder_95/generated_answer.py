def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    sqrt_n = int(n ** 0.5) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(n):
    truncatable_primes = []
    for num in range(2, n):
        if is_prime(num) and all((is_prime(int(str(num)[i:])) for i in range(1, len(str(num))))):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)