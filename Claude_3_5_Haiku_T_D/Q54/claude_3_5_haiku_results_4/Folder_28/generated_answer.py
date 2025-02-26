def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[19]
    truncatable_primes = []
    for num in range(2, x):
        if not is_prime(num):
            continue
        truncatable = True
        current = num
        while current > 0:
            if not is_prime(current):
                truncatable = False
                break
            current //= 10
        if truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)