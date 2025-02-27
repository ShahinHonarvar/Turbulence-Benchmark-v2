def if_perfect_num(nums):
    if sum([i for i in range(1, nums[845]) if nums[845] % i == 0]) == nums[845]:
        return True
    else:
        return False