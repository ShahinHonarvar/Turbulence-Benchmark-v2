def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[38]
    result = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        truncatable = True
        temp_num = num
        while temp_num > 9:
            temp_num //= 10
            if not is_prime(temp_num):
                truncatable = False
                break
        if not truncatable:
            continue
        temp_str = str(num)
        while len(temp_str) > 1:
            temp_str = temp_str[1:]
            if not is_prime(int(temp_str)):
                truncatable = False
                break
        if truncatable:
            result.append(num)
    return result