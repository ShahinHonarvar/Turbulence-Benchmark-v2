def if_perfect_num(nums):
    if sum((i for i in range(1, nums[15]) if nums[15] % i == 0)) == nums[15]:
        return True
    else:
        return False