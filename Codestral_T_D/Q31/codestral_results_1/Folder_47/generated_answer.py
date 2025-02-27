def if_perfect_num(nums):
    if sum([i for i in range(1, nums[34]) if nums[34] % i == 0]) == nums[34]:
        return True
    else:
        return False