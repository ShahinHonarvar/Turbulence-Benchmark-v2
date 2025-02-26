def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[767]
    result = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_left_right_truncatable = True
        temp = num
        while temp > 0:
            if not is_prime(temp):
                is_left_right_truncatable = False
                break
            temp //= 10
        temp = num
        str_temp = str(temp)
        while len(str_temp) > 1:
            str_temp = str_temp[1:]
            temp = int(str_temp)
            if not is_prime(temp):
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable:
            result.append(num)
    return result