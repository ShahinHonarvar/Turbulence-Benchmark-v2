def all_left_right_truncatable_prime(numbers):
    x = numbers[992]
    primes = [n for n in range(x, 0, -1) if is_prime(n)]
    trunc = [n for n in primes if is_left_right_truncatable_prime(n)]
    return trunc

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    sqr = int(n ** 0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if not (n > 1 and (n % 10 != 0 and n != 1)):
        return False
    while n > 9:
        if not is_prime(n):
            return False
        n = int(str(n).replace(str(n[0]), '', 1).replace(str(n[-1]), '', 1))
    return True