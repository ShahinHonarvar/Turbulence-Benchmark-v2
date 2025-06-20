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
    for i in range(1, 10):
        num = i
        while num < n:
            if is_prime(num) and is_prime(num // 10):
                primes.append(num)
                num //= 10
            else:
                break
    return primes

def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:
    x = numbers[945]
    primes = right_truncatable_primes(x)
    return sorted(primes, reverse=True)