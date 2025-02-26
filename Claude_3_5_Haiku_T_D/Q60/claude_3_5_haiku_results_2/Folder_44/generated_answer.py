def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[39]
    result = []
    for n in range(2, x + 1):
        str_n = str(n)
        if '0' in str_n:
            continue
        is_truncatable = True
        for i in range(1, len(str_n)):
            left_trunc = int(str_n[i:])
            right_trunc = int(str_n[:-i])
            if not (is_prime(left_trunc) and is_prime(right_trunc)):
                is_truncatable = False
                break
        if is_truncatable and is_prime(n):
            result.append(n)
    return sorted(result)