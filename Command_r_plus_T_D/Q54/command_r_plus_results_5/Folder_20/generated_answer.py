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
        while num:
            if not is_prime(num):
                break
            num //= 10
        else:
            primes.append(i)
    return primes

def all_right_truncatable_prime(limit):
    result = []
    for i in range(3, limit + 1):
        if i in right_truncatable_primes(len(str(i))):
            result.append(i)
    return sorted(result, reverse=True)