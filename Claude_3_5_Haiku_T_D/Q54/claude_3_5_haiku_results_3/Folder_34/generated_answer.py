def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[18]
    right_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            truncatable = True
            truncated = num
            while truncated > 0:
                truncated //= 10
                if truncated > 0 and (not is_prime(truncated)):
                    truncatable = False
                    break
            if truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)