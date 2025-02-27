def find_second_smallest_num(nums):
    if len(nums[209:557]) < 2:
        return None
    return sorted(nums[209:557])[1]