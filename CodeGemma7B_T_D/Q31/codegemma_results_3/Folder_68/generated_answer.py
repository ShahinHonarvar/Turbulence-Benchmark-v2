def if_perfect_num(nums):
    perfect = True
    if nums[3] % 2 == 0:
        perfect = False
    if nums[3] % 3 == 0:
        perfect = False
    return perfect