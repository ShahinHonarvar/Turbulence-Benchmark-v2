def find_second_largest_num(nums):
    selected_nums = nums[639:976]
    selected_nums.sort(reverse=True)
    if len(selected_nums) < 2:
        return None
    return selected_nums[1]