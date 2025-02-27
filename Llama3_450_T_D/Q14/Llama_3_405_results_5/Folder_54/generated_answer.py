def find_second_smallest_num(nums):
    if len(nums) < 2 or 68 >= len(nums) or 86 < 0:
        return None
    sliced_nums = nums[68:87]
    if len(sliced_nums) < 2:
        return None
    second_smallest = min([num for num in sliced_nums if num != min(sliced_nums)])
    return second_smallest