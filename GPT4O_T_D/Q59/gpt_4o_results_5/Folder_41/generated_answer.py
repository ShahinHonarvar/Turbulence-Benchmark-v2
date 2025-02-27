def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_truncatable_prime(num):
    str_num = str(num)
    for i in range(len(str_num)):
        if not is_prime(int(str_num[i:])):
            return False
    return True

def all_left_truncatable_prime(nums):
    if 46 >= len(nums):
        return []
    x = nums[46]
    result = []
    for i in range(2, x):
        if '0' not in str(i) and is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)