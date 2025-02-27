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

def is_left_right_truncatable(n):
    if '0' in str(n):
        return False
    str_n = str(n)
    while len(str_n) > 0:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[1:]
    str_n = str(n)
    while len(str_n) > 0:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[:-1]
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[86]
    lr_truncatables = []
    for i in range(10, x + 1):
        if is_left_right_truncatable(i):
            lr_truncatables.append(i)
    return sorted(lr_truncatables, reverse=True)