def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[41]
    result = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_left_right_truncatable = True
        temp = num
        while temp > 9:
            temp //= 10
            if not is_prime(temp):
                is_left_right_truncatable = False
                break
        temp = num
        str_num = str(num)
        while len(str_num) > 1:
            str_num = str_num[1:]
            temp_num = int(str_num)
            if not is_prime(temp_num):
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable and is_prime(num):
            result.append(num)
    return result