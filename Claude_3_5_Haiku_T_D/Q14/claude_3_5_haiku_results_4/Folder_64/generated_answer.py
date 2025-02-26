def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) < 5:
        return None
    sublist = nums[0:5]
    sorted_sublist = sorted(set(sublist))
    return sorted_sublist[1] if len(sorted_sublist) >= 2 else None