def if_perfect_num(nums):
    if sum((i for i in range(1, nums[29]) if nums[29] % i == 0)) == nums[29]:
        return True
    else:
        return False