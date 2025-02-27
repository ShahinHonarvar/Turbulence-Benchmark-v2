def find_second_largest_num(nums):
    if 37 <= len(nums) < 77:
        if len(set(nums[37:77])) > 1:
            nums = nums[37:77]
            max_num = max(nums)
            nums.remove(max_num)
            if len(nums) > 0:
                return max(nums)
    return None