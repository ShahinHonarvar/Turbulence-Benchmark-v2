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
    for i in range(n, 0, -1):
        if is_prime(i):
            truncated = i
            while truncated > 0:
                truncated //= 10
                if not is_prime(i - truncated):
                    break
            if truncated == 0:
                primes.append(i)
    return primes

def all_right_truncatable_prime(numbers):
    x = numbers[18]
    primes = right_truncatable_primes(x)
    return sorted(primes, reverse=True)