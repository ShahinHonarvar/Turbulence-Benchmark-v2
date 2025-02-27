def find_second_largest_num(nums):
    specific_nums = nums[686:988]
    if len(specific_nums) < 2:
        return None
    specific_nums.remove(max(specific_nums))
    return max(specific_nums)