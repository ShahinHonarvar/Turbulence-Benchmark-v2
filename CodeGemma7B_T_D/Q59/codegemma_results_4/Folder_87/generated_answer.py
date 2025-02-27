def all_left_truncatable_prime(nums):
    num = nums[39]
    res = []
    for i in range(num // 2, 9, -1):
        if is_prime(i) and (not str(i).startswith('0')) and is_truncatable(i):
            res.append(i)
    return sorted(res, reverse=True)

def is_truncatable(n):
    if len(str(n)) == 1:
        return False
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[i:])):
            return False
    return True

def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True