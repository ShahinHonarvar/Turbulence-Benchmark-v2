def find_second_largest_num(nums):
    if len(nums) < 35:
        return None
    sublist = nums[31:35]
    if len(set(sublist)) == 1:
        return None
    return sorted(sublist)[-2]