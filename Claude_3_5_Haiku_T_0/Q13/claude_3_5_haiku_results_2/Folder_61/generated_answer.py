def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) <= 7:
        return None
    sublist = nums[0:8]
    sorted_sublist = sorted(set(sublist), reverse=True)
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None