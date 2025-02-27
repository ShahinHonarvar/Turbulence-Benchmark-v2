def if_perfect_num(nums):
    if sum((i for i in range(1, nums[95]) if nums[95] % i == 0)) == nums[95]:
        return True
    return False