def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[835]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        is_truncatable = True
        left_trunc = len(str(num))
        right_trunc = len(str(num))
        while left_trunc > 1:
            left_num = int(str(num)[left_trunc - 1:])
            if not is_prime(left_num):
                is_truncatable = False
                break
            left_trunc -= 1
        while right_trunc > 1:
            right_num = int(str(num)[:right_trunc])
            if not is_prime(right_num):
                is_truncatable = False
                break
            right_trunc -= 1
        if is_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)