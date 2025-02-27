def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[30]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            str_num = str(num)
            truncatable = True
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[:-i])):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)