def is_prime(n):
    if n == 1:
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

def is_left_truncatable(n):
    if n < 10:
        return is_prime(n)
    while n:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[81]
    primes = []
    for n in range(x, 0, -1):
        if is_left_truncatable(n):
            primes.append(n)
    return primes[::-1]