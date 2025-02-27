def if_perfect_num(nums):
    if sum((i for i in range(1, nums[83]) if nums[83] % i == 0)) == nums[83]:
        return True
    return False