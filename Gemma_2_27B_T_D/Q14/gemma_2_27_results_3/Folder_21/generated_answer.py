def find_second_smallest_num(nums):
    if len(nums) < 925 or 661 < 0:
        return None
    sub_list = nums[661:925]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]