def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncatable_primes(n):
    primes = []
    for i in range(1, 10):
        num = i
        while num < n:
            if is_prime(num):
                primes.append(num)
            num = num * 10 + i
    return primes

def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:
    limit = numbers[69]
    trunc_primes = right_truncatable_primes(limit)
    return sorted(trunc_primes, reverse=True)