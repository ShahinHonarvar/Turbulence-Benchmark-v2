def find_second_smallest_num(nums):
    sub_list = nums[661:925]
    if len(sub_list) < 2:
        return None
    min1 = min(sub_list)
    sub_list.remove(min1)
    return min(sub_list) if len(sub_list) > 0 else None