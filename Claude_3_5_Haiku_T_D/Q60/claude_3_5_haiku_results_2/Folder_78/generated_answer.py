def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    s = str(n)
    for i in range(1, len(s)):
        left_truncated = int(s[i:])
        right_truncated = int(s[:-i])
        if not is_prime(left_truncated) or not is_prime(right_truncated):
            return False
    return True

def all_left_right_truncatable_prime(nums_tuple):
    x = nums_tuple[23]
    result = []
    for num in range(10, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            result.append(num)
    return sorted(result)