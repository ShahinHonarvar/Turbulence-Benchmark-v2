def find_second_largest_num(nums):
    arr = nums[28:41]
    if len(arr) < 2:
        return None
    return sorted(arr)[-2]