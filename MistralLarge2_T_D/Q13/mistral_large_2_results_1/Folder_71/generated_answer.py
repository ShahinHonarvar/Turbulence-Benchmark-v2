def find_second_largest_num(nums):
    selected_nums = nums[26:53]
    if len(selected_nums) < 2:
        return None
    first_largest = max(selected_nums)
    selected_nums.remove(first_largest)
    second_largest = max(selected_nums)
    return second_largest