def find_second_largest_num(nums):
    section_nums = nums[75:89]
    if len(section_nums) < 2:
        return None
    else:
        max_num = max(section_nums)
        section_nums.remove(max_num)
        second_max_num = max(section_nums)
        return second_max_num