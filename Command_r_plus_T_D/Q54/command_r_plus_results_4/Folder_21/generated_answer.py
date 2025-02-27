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
    if n < 10:
        return [n for n in range(2, n + 1) if is_prime(n)]
    else:
        primes = [n for n in range(2, 10) if is_prime(n)]
        for i in range(9, n - 1, -1):
            if is_prime(i):
                for p in primes:
                    num = p * 10 + i
                    if is_prime(num):
                        primes.append(num)
        return primes

def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:
    x = numbers[175]
    primes = right_truncatable_primes(x)
    return sorted([p for p in primes if p < x])