def find_second_smallest_num(nums):
    if 30 <= len(nums) <= 48:
        sub_list = nums[30:49]
        sub_list.sort()
        return sub_list[1] if len(sub_list) > 1 else None
    return None