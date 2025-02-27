def find_second_largest_num(nums):
    if 639 <= len(nums) <= 975:
        nums = nums[638:976]
        if len(nums) > 1:
            max_num = max(nums)
            nums.remove(max_num)
            if len(nums) > 1:
                return max(nums)
    return None