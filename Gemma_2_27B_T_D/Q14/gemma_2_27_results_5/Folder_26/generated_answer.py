def find_second_smallest_num(nums):
    if len(nums[62:79]) < 2:
        return None
    sorted_nums = sorted(nums[62:79])
    return sorted_nums[1]