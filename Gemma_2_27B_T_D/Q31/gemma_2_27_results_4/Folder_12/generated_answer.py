def if_perfect_num(nums):
    if sum((i for i in range(1, nums[27]) if nums[27] % i == 0)) == nums[27]:
        return True
    else:
        return False