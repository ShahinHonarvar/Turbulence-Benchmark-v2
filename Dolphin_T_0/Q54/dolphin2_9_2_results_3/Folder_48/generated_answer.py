def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(nums):
    x = nums[835]
    res = []
    for i in range(x):
        if is_prime(i):
            trunc = i
            while trunc != 0:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                res.append(i)
    res.sort()
    return res