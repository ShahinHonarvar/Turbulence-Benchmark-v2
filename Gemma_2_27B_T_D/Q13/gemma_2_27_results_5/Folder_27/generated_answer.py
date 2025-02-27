def find_second_largest_num(nums):
    if len(nums) < 94:
        return None
    sub_list = nums[66:94]
    if len(set(sub_list)) < 2:
        return None
    return sorted(set(sub_list))[-2]