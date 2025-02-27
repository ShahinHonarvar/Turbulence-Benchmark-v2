def find_second_smallest_num(nums):
    subsection = nums[68:87]
    unique_nums = list(set(subsection))
    unique_nums.sort()
    if len(unique_nums) < 2:
        return None
    else:
        return unique_nums[1]