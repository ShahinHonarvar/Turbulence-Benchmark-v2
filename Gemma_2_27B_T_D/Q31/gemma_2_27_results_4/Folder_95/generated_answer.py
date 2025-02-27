def if_perfect_num(nums):
    if nums[87] == sum([i for i in range(1, nums[87]) if nums[87] % i == 0]):
        return True
    else:
        return False