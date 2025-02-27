def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n, primes):
    for digit in str(n):
        if n != int(digit) and n % int(digit) == 0 and (is_prime(n // int(digit)) not in primes):
            return False
    return True

def all_right_truncatable_prime(nums):
    if isinstance(nums, tuple) and all((isinstance(i, int) and i > 0 for i in nums)):
        x = nums[42]
        primes = [x for x in range(2, x) if is_prime(x)]
        right_truncatable_primes = [x for x in primes if is_right_truncatable(x, primes)]
        return sorted(right_truncatable_primes)
    else:
        return []