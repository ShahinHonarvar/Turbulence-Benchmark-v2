def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[61]
    right_truncatable_primes = []
    for n in range(2, x):
        if is_prime(n):
            truncatable = True
            num_str = str(n)
            while len(num_str) > 1:
                num_str = num_str[:-1]
                truncated_num = int(num_str)
                if not is_prime(truncated_num):
                    truncatable = False
                    break
            if truncatable:
                right_truncatable_primes.append(n)
    return sorted(right_truncatable_primes)