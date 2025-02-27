def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[100]
    primes = []
    for n in range(x - 1, 0, -1):
        if is_prime(n) and is_right_truncatable(n):
            primes.append(n)
    primes.sort(reverse=True)
    return primes