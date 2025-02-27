def find_second_smallest_num(nums):
    section = nums[62:100]
    if len(section) < 2:
        return None
    else:
        section.sort()
        return section[1]