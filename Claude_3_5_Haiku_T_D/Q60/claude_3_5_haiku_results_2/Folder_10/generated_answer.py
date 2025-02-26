def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[38]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_truncatable = True
        right_trunc = num
        while right_trunc > 9:
            right_trunc //= 10
            if not is_prime(right_trunc):
                is_truncatable = False
                break
        left_trunc = num
        digit_length = len(str(left_trunc))
        while left_trunc > 9:
            left_trunc %= 10 ** (digit_length - 1)
            digit_length -= 1
            if not is_prime(left_trunc):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)