def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[1]
    result = []

    def is_truncatable(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(len(str_num)):
            left_trunc = int(str_num[i:])
            right_trunc = int(str_num[:len(str_num) - i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
        return True
    for num in range(x, 11, -1):
        if is_prime(num) and is_truncatable(num):
            result.append(num)
    return result