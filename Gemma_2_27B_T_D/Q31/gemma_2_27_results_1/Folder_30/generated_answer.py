def if_perfect_num(nums):
    if sum([i for i in range(1, nums[94]) if nums[94] % i == 0]) == nums[94]:
        return True
    else:
        return False