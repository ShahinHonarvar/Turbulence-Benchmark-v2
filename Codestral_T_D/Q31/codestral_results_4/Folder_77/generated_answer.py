def if_perfect_num(nums):
    if sum((i for i in range(1, nums[985]) if nums[985] % i == 0)) == nums[985]:
        return True
    else:
        return False