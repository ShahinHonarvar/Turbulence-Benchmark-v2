def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[792]
    left_truncatable_primes = []
    for num in range(2, x):
        is_truncatable = True
        str_num = str(num)
        if '0' in str_num:
            continue
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)