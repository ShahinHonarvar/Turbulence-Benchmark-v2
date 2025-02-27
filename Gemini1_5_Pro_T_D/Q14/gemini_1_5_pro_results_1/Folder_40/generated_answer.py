def find_second_smallest_num(nums):
    if len(nums) < 3:
        sub_list = nums
    else:
        sub_list = nums[:3]
    sorted_list = sorted(sub_list)
    if len(sorted_list) < 2:
        return None
    else:
        return sorted_list[1]