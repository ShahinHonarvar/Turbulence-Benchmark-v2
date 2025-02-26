def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[74]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        is_left_right_truncatable = True
        right_trunc_num = num
        while right_trunc_num > 0:
            if not is_prime(right_trunc_num):
                is_left_right_truncatable = False
                break
            right_trunc_num //= 10
        if not is_left_right_truncatable:
            continue
        left_trunc_str = str(num)
        while len(left_trunc_str) > 0:
            if not is_prime(int(left_trunc_str)):
                is_left_right_truncatable = False
                break
            left_trunc_str = left_trunc_str[1:]
        if is_left_right_truncatable:
            result.append(num)
    return sorted(result)