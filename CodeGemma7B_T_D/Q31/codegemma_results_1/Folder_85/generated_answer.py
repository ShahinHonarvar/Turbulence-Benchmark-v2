def if_perfect_num(nums):
    num = nums[22]
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True