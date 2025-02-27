def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def is_right_truncatable_prime(num):
    for digit in str(num):
        if not is_prime(int(digit)):
            return False
        num = num // 10
    return is_prime(num)

def all_right_truncatable_prime(nums):
    max_num = nums[429]
    res = []
    for i in range(max_num, 1, -1):
        if is_right_truncatable_prime(i):
            res.append(i)
    return res