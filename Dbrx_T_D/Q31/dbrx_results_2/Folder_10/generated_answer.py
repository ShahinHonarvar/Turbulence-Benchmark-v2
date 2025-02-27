def if_perfect_num(nums):
    if len(nums) > 54 and 54 >= 0:
        return nums[54] == sum([i for i in range(1, nums[54]) if nums[54] % i == 0])
    else:
        return False