def find_second_smallest_num(nums):
    if len(nums) < 8:
        return None
    selected_nums = nums[5:8]
    selected_nums.sort()
    if len(selected_nums) < 2:
        return None
    return selected_nums[1]