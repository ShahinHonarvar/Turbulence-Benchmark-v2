def if_perfect_num(nums):
    if sum([i for i in range(1, nums[35]) if nums[35] % i == 0]) == nums[35]:
        return True
    else:
        return False