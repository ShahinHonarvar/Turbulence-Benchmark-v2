def find_second_smallest_num(nums):
    subset = nums[5:9]
    if len(set(subset)) < 2:
        return None
    return sorted(subset)[1]