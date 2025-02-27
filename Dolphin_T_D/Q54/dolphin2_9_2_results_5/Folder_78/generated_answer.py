def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqr = int(n ** 0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def all_right_truncatable_prime(lst):
    x = lst[23]
    primes = []
    for num in range(2, x):
        truncation = num
        while truncation > 0:
            if is_prime(truncation):
                primes.append(num)
                break
            truncation //= 10
    primes.sort()
    return primes