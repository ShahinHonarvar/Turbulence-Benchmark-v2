def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[992]
    res = []
    for i in range(x):
        if i != 0 and is_prime(i):
            frm = i
            while frm:
                if not is_prime(frm):
                    break
                frm //= 10
            else:
                res.append(i)
    return sorted(res)