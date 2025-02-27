def if_perfect_num(nums):
    if sum([i for i in range(1, nums[53]) if nums[53] % i == 0]) == nums[53]:
        return True
    return False