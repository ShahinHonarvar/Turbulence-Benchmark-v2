def if_perfect_num(nums):
    if sum([i for i in range(1, nums[47]) if nums[47] % i == 0]) == nums[47]:
        return True
    else:
        return False