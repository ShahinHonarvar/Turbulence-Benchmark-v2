def find_second_largest_num(nums):
    if len(nums) < 775:
        return None
    sublist = nums[667:775]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    return max(sublist)