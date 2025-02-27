def find_second_largest_num(nums):
    selected_nums = nums[686:988]
    if len(selected_nums) < 2:
        return None
    sorted_nums = sorted(selected_nums)
    return sorted_nums[-2]