def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[70]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)

def is_truncatable_prime(num):
    str_num = str(num)
    for i in range(len(str_num)):
        left_trunc = int(str_num[i:])
        right_trunc = int(str_num[:len(str_num) - i])
        if not is_prime(left_trunc) or not is_prime(right_trunc):
            return False
    return True