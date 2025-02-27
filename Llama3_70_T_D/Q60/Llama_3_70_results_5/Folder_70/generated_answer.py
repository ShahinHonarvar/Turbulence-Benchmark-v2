def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[433]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        str_num = str(num)
        left_truncatable = True
        right_truncatable = True
        for i in range(1, len(str_num)):
            left_trunc = int(str_num[i:])
            right_trunc = int(str_num[:-i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                left_truncatable = False
                right_truncatable = False
                break
        if left_truncatable and right_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)