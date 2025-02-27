def if_perfect_num(nums):
    n = nums[93]
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i == n // i:
                n += i - 1
            else:
                n += i + n // i
    return n == 1