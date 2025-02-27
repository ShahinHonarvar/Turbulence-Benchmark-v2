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
    for i in range(10 ** len(str(n)), n, -1):
        if is_prime(i):
            truncated_prime = i
            while truncated_prime > 9:
                truncated_prime //= 10
                if not is_prime(truncated_prime):
                    break
            if truncated_prime == 9:
                primes.append(i)
    return sorted(primes, reverse=True)

def all_right_truncatable_prime(numbers):
    x = numbers[86]
    return right_truncatable_primes(x)