def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[84]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num) and is_prime(num):
            truncatable = True
            truncated_num = str(num)
            while len(truncated_num) > 1:
                truncated_num = truncated_num[1:]
                if not is_prime(int(truncated_num)):
                    truncatable = False
                    break
            if truncatable:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)