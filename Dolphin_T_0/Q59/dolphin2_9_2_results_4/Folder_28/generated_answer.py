def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(x):
    res = []
    nums = list(map(int, str(x)))
    for i in range(1, len(nums)):
        temp = []
        for j in range(10 ** i):
            temp.append(j * 10 ** (len(nums) - i) + int(''.join(map(str, nums[i:]))))
        for k in temp:
            if k < x and is_prime(k):
                res.append(k)
    return sorted(list(set(res)))