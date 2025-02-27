def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    if n < 2:
        return False
    while n > 2:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return True

def all_right_truncatable_prime(nums):
    x = nums[54]
    primes = [n for n in range(x - 1, 0, -1) if is_right_truncatable_prime(n)]
    return primes