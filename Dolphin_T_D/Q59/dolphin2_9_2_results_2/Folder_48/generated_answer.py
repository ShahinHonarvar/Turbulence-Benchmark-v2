def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[835]
    primes = []
    for n in range(2, x):
        if is_prime(n):
            orig = n
            while n != 0:
                n //= 10
            if is_prime(orig):
                primes.append(orig)
    return sorted(primes)