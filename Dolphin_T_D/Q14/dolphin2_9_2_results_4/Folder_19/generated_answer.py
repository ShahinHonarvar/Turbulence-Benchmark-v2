def find_second_smallest_num(nums):
    subsection = nums[4:9]
    if len(set(subsection)) < 2:
        return None
    else:
        min_num = min(subsection)
        subsection.remove(min_num)
        return min(subsection)