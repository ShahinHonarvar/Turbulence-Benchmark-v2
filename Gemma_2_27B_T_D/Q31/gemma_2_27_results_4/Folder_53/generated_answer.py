def if_perfect_num(nums):
    if sum([i for i in range(1, nums[73]) if nums[73] % i == 0]) == nums[73]:
        return True
    return False