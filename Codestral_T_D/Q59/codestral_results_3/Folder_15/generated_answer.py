def all_left_truncatable_prime(numbers):
    x = numbers[6]
    primes = [p for p in range(2, x) if all((is_prime(int(str(p)[i:])) for i in range(len(str(p)))))]
    return sorted(primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True