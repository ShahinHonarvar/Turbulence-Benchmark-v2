def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[41]
    truncatable_primes = []
    for num in range(10, x):
        str_num = str(num)
        is_truncatable = True
        for i in range(len(str_num), 0, -1):
            if not is_prime(int(str_num[:i])):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)