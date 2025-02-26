def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    if '0' in str(num):
        return False
    while num > 9:
        num_str = str(num)
        num_str_left = num_str[1:]
        num_str_right = num_str[:-1]
        left_trunc = int(num_str_left)
        right_trunc = int(num_str_right)
        if not (is_prime(left_trunc) and is_prime(right_trunc)):
            return False
        num = left_trunc
    return is_prime(num)

def all_left_right_truncatable_prime(nums):
    x = nums[89]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes