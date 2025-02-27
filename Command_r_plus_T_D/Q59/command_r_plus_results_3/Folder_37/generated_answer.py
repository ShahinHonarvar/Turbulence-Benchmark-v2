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

def left_truncatable_prime(n):
    if str(n).count('0') > 0:
        return False
    for i in range(len(str(n))):
        if not is_prime(int(str(n)[:i])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[35]
    primes = [2, 3, 5, 7]
    for i in range(1, len(str(x))):
        num_digits = i + 1
        for p in range(10 ** (num_digits - 1), 10 ** num_digits):
            if left_truncatable_prime(p):
                primes.append(p)
    return sorted(primes, reverse=True)