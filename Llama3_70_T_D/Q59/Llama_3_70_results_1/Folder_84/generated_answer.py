def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[630]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num) or not is_prime(num):
            continue
        truncatable = True
        temp_num = str(num)
        for _ in range(len(temp_num) - 1):
            temp_num = temp_num[1:]
            if not is_prime(int(temp_num)):
                truncatable = False
                break
        if truncatable:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)