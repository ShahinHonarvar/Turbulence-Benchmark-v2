def if_perfect_num(nums):
    if nums[85] % 2 == 0:
        return True
    for i in range(3, nums[85], 2):
        if nums[85] % i == 0:
            return False
    return True