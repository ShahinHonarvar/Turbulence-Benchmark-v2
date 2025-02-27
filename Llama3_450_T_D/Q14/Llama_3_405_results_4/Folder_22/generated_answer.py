def find_second_smallest_num(nums):
    specific_nums = nums[40:201]
    if len(specific_nums) < 2:
        return None
    else:
        specific_nums.remove(min(specific_nums))
        return min(specific_nums)