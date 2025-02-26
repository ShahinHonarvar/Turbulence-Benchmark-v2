def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[64]
    result = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_truncatable = True
        original_num = num
        while num >= 10:
            num = int(str(num)[1:])
            if not is_prime(num):
                is_truncatable = False
                break
        if not is_prime(num):
            is_truncatable = False
        num = original_num
        str_num = str(num)
        while len(str_num) > 1:
            str_num = str_num[:-1]
            if not is_prime(int(str_num)):
                is_truncatable = False
                break
        if is_truncatable and is_prime(original_num):
            result.append(original_num)
    return result