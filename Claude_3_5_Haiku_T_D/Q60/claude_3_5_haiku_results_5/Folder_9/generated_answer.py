def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    str_num = str(num)
    if '0' in str_num:
        return False
    for length in range(len(str_num), 0, -1):
        left_trunc = int(str_num[-length:])
        right_trunc = int(str_num[:length])
        while len(str(left_trunc)) > 1:
            if not is_prime(left_trunc):
                return False
            left_trunc //= 10
        while len(str(right_trunc)) > 1:
            if not is_prime(right_trunc):
                return False
            right_trunc //= 10
        if not is_prime(left_trunc) or not is_prime(right_trunc):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[29]
    truncatable_primes = [num for num in range(2, x + 1) if is_prime(num) and is_left_right_truncatable_prime(num)]
    return sorted(truncatable_primes, reverse=True)