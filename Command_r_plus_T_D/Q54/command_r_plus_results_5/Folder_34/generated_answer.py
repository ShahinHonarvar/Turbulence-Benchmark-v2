def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncatable_primes(n):
    primes = []
    for i in range(10 ** len(str(n)), n + 1):
        truncable = True
        num = i
        while num > 9:
            num //= 10
            if not is_prime(num):
                truncable = False
                break
        if truncable and is_prime(i):
            primes.append(i)
    return primes

def all_right_truncatable_prime(numbers):
    x = numbers[18]
    primes = right_truncatable_primes(x)
    return sorted(primes, reverse=True)