def find_second_largest_num(nums):
    sub_list = nums[40:81]
    if len(sub_list) < 2:
        return None
    return sorted(set(sub_list))[-2]