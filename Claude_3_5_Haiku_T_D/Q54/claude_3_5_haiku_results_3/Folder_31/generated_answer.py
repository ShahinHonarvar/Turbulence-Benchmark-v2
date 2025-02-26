def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[50]
    right_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            num_str = str(num)
            is_right_truncatable = True
            for length in range(len(num_str) - 1, 0, -1):
                truncated = int(num_str[:length])
                if not is_prime(truncated):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)