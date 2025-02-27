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
    for i in range(10 ** n, 10 ** (n - 1), -1):
        num = i
        while num > 9:
            if not is_prime(num):
                break
            num //= 10
        else:
            if is_prime(num):
                primes.append(i)
    return primes

def all_right_truncatable_prime(numbers):
    x = numbers[28]
    primes = right_truncatable_primes(len(str(x)))
    return sorted([p for p in primes if p < x])