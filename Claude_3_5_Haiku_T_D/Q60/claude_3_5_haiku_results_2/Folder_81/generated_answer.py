def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums_tuple):
    x = nums_tuple[98]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if is_truncatable_prime(num):
            result.append(num)
    return sorted(result)

def is_truncatable_prime(num):
    s = str(num)
    for i in range(len(s)):
        left_trunc = int(s[i:])
        right_trunc = int(s[:len(s) - i])
        if not (is_prime(left_trunc) and is_prime(right_trunc)):
            return False
    return True