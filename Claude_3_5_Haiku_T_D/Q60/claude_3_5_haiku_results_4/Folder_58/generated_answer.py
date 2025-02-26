def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[975]
    result = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_truncatable = True
        full_num = num
        while num > 9:
            num //= 10
            if not is_prime(num):
                is_truncatable = False
                break
        if not is_truncatable or not is_prime(num):
            continue
        num = full_num
        while num > 9:
            num %= 10 ** (len(str(num)) - 1)
            if not is_prime(num):
                is_truncatable = False
                break
        if is_truncatable and is_prime(full_num):
            result.append(full_num)
    return result