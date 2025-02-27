def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_right_truncatable_prime(n):
    while n:
        if n % 10 == 0:
            return False
        if not is_prime(int(str(n)[-1])):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(nums):
    x = nums[992]
    primes = []
    for n in range(2, x):
        if is_right_truncatable_prime(n):
            primes.append(n)
    return sorted(primes)