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

def left_truncatable_prime(num):
    for i in range(1, len(num)):
        if not is_prime(int(num[i:])):
            return False
    return True

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[79]
    primes = []
    for i in range(2, x):
        if left_truncatable_prime(str(i)):
            primes.append(i)
    return sorted(primes, reverse=True)