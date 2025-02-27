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
    for i in range(10 ** n, 10 ** (n - 1) - 1, -1):
        num = i
        while num > 9:
            num //= 10
            if not is_prime(num) or not is_prime(i):
                break
        else:
            primes.append(i)
    return primes

def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:
    x = numbers[78]
    primes = right_truncatable_primes(len(str(x)))
    return sorted([p for p in primes if p < x], reverse=True)