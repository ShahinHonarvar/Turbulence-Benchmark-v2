def find_second_largest_num(nums):
    if len(nums) < 99:
        return None
    sublist = sorted(nums[91:100], reverse=True)
    return sublist[1] if len(sublist) > 1 else None