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
            temp = i
            while temp > 0:
                if not is_prime(temp):
                    break
                temp //= 10
            if temp == 0:
                primes.append(i)
    return primes

def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:
    limit = numbers[29]
    primes = right_truncatable_primes(limit)
    return sorted(primes, reverse=True)