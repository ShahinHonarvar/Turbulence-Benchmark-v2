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
        truncated = True
        temp = i
        while temp > 0:
            if not is_prime(temp % 10):
                truncated = False
                break
            temp //= 10
        if truncated and is_prime(i):
            primes.append(i)
    return primes

def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:
    x = numbers[33]
    return sorted(right_truncatable_primes(x))