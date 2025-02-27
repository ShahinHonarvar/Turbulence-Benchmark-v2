def all_left_truncatable_prime(numbers):
    x = numbers[70]
    left_truncatable_primes = []
    for i in range(x):
        if i != 0 and i % 2 != 0 and (i % 5 != 0):
            if is_prime(i) and i != 0 and is_left_truncatable(i):
                left_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 2
    return True

def is_left_truncatable(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return True