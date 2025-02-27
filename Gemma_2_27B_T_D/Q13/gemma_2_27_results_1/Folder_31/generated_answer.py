def find_second_largest_num(nums):
    if len(nums) < 88 or len(nums) < 75:
        return None
    sub_list = nums[75:89]
    try:
        return sorted(sub_list)[-2]
    except IndexError:
        return None