def if_perfect_num(nums):
    if sum((i for i in range(1, nums[91]) if nums[91] % i == 0)) == nums[91]:
        return True
    return False