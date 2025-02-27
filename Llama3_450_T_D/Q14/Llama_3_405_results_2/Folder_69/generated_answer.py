def find_second_smallest_num(nums):
    if len(nums) < 88 or not all((isinstance(x, (int, float)) for x in nums)):
        return None
    selected_nums = sorted(nums[25:88])
    if len(selected_nums) < 2:
        return None
    return selected_nums[1]