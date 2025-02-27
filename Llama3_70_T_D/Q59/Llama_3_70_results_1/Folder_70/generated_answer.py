def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[433]
    left_truncatable_primes = []
    for num in range(10, x):
        if '0' not in str(num):
            truncatable = num
            while truncatable > 0:
                if not is_prime(truncatable):
                    break
                truncatable //= 10
            else:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)