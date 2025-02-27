def all_left_truncatable_prime(nums):
    x = nums[14]
    res = []
    for num in range(2, x):
        if is_prime(num) and (not has_zero(num)):
            str_num = str(num)
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[i:])):
                    break
            else:
                res.append(num)
    return sorted(res)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def has_zero(num):
    return '0' in str(num)