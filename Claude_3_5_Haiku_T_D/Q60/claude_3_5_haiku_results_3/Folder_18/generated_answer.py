def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[429]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_left_right_truncatable = True
        current_num = num
        while current_num > 9:
            current_num_str = str(current_num)
            left_truncated = int(current_num_str[1:])
            right_truncated = int(current_num_str[:-1])
            if not (is_prime(left_truncated) and is_prime(right_truncated)):
                is_left_right_truncatable = False
                break
            current_num = left_truncated
        if is_left_right_truncatable and is_prime(current_num) and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)