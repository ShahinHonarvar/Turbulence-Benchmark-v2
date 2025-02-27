def if_perfect_num(nums):
    if nums[0] % 2 == 0 or not nums:
        return False
    for i in range(3, nums[0], 2):
        if nums[0] % i == 0:
            return False
    return True