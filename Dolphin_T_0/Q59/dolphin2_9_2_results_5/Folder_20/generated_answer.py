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

def is_left_truncatable_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return is_prime(n)
    if n % 10 == 0:
        return False
    while n > 1:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(nums):
    x = nums[100]
    primes = []
    for num in range(x, 0, -1):
        if is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)