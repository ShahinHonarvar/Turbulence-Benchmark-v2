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
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_left_right_truncatable = True
        for length in range(len(str(num)), 0, -1):
            truncated_left = int(str(num)[length - 1:])
            truncated_right = int(str(num)[:length])
            if not (is_prime(truncated_left) and is_prime(truncated_right)):
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes