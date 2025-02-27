def all_left_truncatable_prime(numbers):
    x = numbers[88]
    primes = []
    for n in range(2, x):
        if all((is_prime(int(str(n)[i:])) for i in range(len(str(n))))):
            primes.append(n)
    return sorted(primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True