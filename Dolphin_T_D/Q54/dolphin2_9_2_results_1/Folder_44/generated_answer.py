import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    sqrt_n = math.sqrt(n)
    for i in range(3, int(sqrt_n) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[39]
    result = []
    for num in range(2, x):
        if is_prime(num):
            str_num = str(num)
            for i in range(len(str_num) - 1, 0, -1):
                if is_prime(int(str_num[0:i])):
                    result.append(num)
                    break
    return sorted(list(set(result)))