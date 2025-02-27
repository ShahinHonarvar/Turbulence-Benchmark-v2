def find_second_largest_num(nums):
    if len(nums) < 95:
        return None
    selected_nums = nums[75:95]
    if len(selected_nums) < 2:
        return None
    first_largest = max(selected_nums)
    selected_nums.remove(first_largest)
    second_largest = max(selected_nums)
    return second_largest