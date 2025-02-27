def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[466]
    primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if not is_prime(num):
            continue
        truncatable = True
        for i in range(1, len(str_num)):
            left_trunc = int(str_num[i:])
            right_trunc = int(str_num[:-i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                truncatable = False
                break
        if truncatable:
            primes.append(num)
    primes.sort(reverse=True)
    return primes