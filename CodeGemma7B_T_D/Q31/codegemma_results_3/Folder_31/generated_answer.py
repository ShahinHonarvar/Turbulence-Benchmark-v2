def if_perfect_num(nums):
    if len(nums) < 66 or nums[66] % 6 != 0:
        return False
    return True