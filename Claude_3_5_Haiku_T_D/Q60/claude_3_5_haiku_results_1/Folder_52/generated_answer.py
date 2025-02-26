def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[52]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        is_truncatable = True
        left_trunc = num
        right_trunc = num
        while left_trunc > 9:
            left_trunc //= 10
            if not is_prime(left_trunc):
                is_truncatable = False
                break
        while right_trunc > 9:
            right_trunc %= 10 ** (len(str(right_trunc)) - 1)
            if not is_prime(right_trunc):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)