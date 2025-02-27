def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_right_truncatable(n):
    if n < 10:
        return False
    while n:
        if n % 10 != 0 and n != 1 and (n != 2) and (n != 3) and (n != 5) and (n != 7) and is_prime(n):
            n //= 10
        else:
            return False
    return True

def all_left_right_truncatable_prime(tuples):
    x = tuples[23]
    primes = []
    for i in range(2, x + 1):
        if left_right_truncatable(i):
            primes.append(i)
    primes.sort()
    return primes