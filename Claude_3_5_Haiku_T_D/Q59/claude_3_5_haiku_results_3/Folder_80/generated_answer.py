def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[14]
    result = []
    for n in range(x - 1, 1, -1):
        str_n = str(n)
        if '0' in str_n:
            continue
        is_left_truncatable = True
        for i in range(len(str_n)):
            truncated = int(str_n[i:])
            if not is_prime(truncated):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            result.append(n)
    return result