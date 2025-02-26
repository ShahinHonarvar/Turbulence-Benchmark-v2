def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[52]
    result = []
    for n in range(x, 11, -1):
        if '0' in str(n):
            continue
        is_truncatable = True
        num_str = str(n)
        for i in range(len(num_str)):
            left_truncated = int(num_str[i:])
            right_truncated = int(num_str[:len(num_str) - i])
            if not (is_prime(left_truncated) and is_prime(right_truncated)):
                is_truncatable = False
                break
        if is_truncatable and is_prime(n):
            result.append(n)
    return sorted(result, reverse=True)