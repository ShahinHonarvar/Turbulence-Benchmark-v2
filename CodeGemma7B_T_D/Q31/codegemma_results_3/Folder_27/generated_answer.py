def if_perfect_num(nums):
    n = nums[56]
    perfect = False
    if n % 2 == 0:
        perfect = True
    else:
        for i in range(3, n, 2):
            if n % i == 0:
                perfect = True
                break
    return perfect