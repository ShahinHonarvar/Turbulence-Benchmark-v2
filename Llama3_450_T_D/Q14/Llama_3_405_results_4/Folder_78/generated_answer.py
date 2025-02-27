def find_second_smallest_num(nums):
    if len(nums) < 79:
        return None
    selected_nums = nums[17:79]
    selected_nums.sort()
    if len(selected_nums) < 2:
        return None
    return selected_nums[1]