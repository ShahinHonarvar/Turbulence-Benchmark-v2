def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[20]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_truncatable = True
        left_str = str(num)
        right_str = str(num)
        while len(left_str) > 1:
            left_str = left_str[1:]
            right_str = right_str[:-1]
            left_val = int(left_str)
            right_val = int(right_str)
            if not (is_prime(left_val) and is_prime(right_val)):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)