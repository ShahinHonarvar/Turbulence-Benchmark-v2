def if_perfect_num(nums):
    if nums[92] % 2 == 0 and nums[92] / 2 in nums:
        return True
    if nums[92] % 3 == 0 and nums[92] / 3 in nums:
        return True
    if nums[92] % 5 == 0 and nums[92] / 5 in nums:
        return True
    return False