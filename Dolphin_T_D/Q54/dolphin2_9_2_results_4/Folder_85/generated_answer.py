def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[94]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j != 0 and is_prime(j):
                j //= 10
            if j == 0:
                primes.append(i)
    return sorted(primes)