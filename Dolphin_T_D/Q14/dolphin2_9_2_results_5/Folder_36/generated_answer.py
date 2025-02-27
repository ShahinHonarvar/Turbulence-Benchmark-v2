def find_second_smallest_num(nums):
    section = nums[209:557]
    if len(section) < 2:
        return None
    section.sort()
    return section[1]