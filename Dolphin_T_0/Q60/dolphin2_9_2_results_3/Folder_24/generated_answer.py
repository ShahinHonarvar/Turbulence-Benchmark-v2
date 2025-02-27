def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(x):
    if not isinstance(x, (int, float)) or x <= 1:
        return []
    digits = set()
    while x > 0:
        digits.add(x % 10)
        x //= 10
    primes = []
    for i in range(len(str(x)), -1, -1):
        for d in digits:
            n = int(str(d) + '0' * i + str(d))
            if n > x or not is_prime(n):
                continue
            primes.append(n)
    return sorted(primes, reverse=True)