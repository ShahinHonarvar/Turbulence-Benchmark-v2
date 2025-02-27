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
    for i in range(10 ** len(str(n)), 10 ** (len(str(n)) - 1) - 1, -1):
        num = i
        while num > 9:
            if is_prime(num):
                num //= 10
            else:
                break
        if num == 1 and is_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)

def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:
    x = numbers[36]
    return right_truncatable_primes(x)