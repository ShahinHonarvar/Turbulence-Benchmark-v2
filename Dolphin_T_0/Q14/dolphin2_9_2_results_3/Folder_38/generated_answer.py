def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    subsection = nums[36:52]
    sorted_subsection = sorted(subsection)
    if len(sorted_subsection) < 2:
        return None
    return sorted_subsection[1]