def if_perfect_num(nums):
    if nums[4] % 2 == 0 and sum((x for x in range(2, nums[4]) if nums[4] % x == 0)) == nums[4] - 2:
        return True
    return False