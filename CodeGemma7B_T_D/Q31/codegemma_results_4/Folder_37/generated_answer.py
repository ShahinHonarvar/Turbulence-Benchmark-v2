def if_perfect_num(nums):
    num = nums[28]
    perfect = False
    for i in range(2, num):
        if num % i == 0:
            perfect = True
            break
    return perfect