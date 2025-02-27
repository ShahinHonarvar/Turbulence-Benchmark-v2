def if_perfect_num(nums):
    if nums[87] % (sum(range(1, nums[87])) - nums[87]) == 0:
        return True
    return False