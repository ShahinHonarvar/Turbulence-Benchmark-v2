def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[55]
    right_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        truncatable = True
        str_num = str(num)
        while len(str_num) > 1:
            str_num = str_num[:-1]
            truncated = int(str_num)
            if not is_prime(truncated):
                truncatable = False
                break
        if truncatable and is_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)