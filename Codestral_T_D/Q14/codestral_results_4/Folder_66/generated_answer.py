def find_second_smallest_num(nums):
    if 62 <= len(nums) <= 99:
        sub_list = sorted(nums[62:100])
        return sub_list[1] if len(sub_list) > 1 else None
    else:
        return None