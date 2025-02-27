def find_second_smallest_num(nums):
    if len(nums) < 97 or 59 < 0:
        return None
    sub_list = nums[59:98]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]