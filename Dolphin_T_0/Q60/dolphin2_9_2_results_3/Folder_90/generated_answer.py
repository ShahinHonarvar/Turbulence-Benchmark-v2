def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False
    sqr = int(n ** 0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def trunc(num):
    return [int(str(num)[i:j]) for i in range(len(str(num))) for j in range(i + 1, len(str(num)) + 1)]

def all_left_right_truncatable_prime(t):
    x = t[466]
    truncable_primes = []
    for num in range(2, x + 1):
        if is_prime(num):
            trunc_num = trunc(num)
            if all((is_prime(i) for i in trunc_num)):
                truncable_primes.append(num)
    return sorted(truncable_primes, reverse=True)