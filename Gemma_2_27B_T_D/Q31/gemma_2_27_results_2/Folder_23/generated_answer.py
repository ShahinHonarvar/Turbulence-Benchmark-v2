def if_perfect_num(nums):
    if sum((i for i in range(1, nums[69]) if nums[69] % i == 0)) == nums[69]:
        return True
    return False