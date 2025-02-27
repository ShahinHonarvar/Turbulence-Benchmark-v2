def find_second_smallest_num(nums):
    if len(nums) < 93 - 66 + 1:
        return None
    sorted_slice = sorted(nums[66:94])
    if len(sorted_slice) >= 2:
        return sorted_slice[1]
    else:
        return None