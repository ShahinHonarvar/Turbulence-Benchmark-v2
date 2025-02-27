def find_second_largest_num(nums):
    if 209 <= len(nums) <= 556:
        nums = nums[209:557]
        max_num = max(nums)
        nums.remove(max_num)
        if len(nums) > 0:
            second_max_num = max(nums)
            return second_max_num
        else:
            return None
    else:
        return None