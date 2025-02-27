def find_second_largest_num(nums):
    if len(nums) < 6:
        return None
    sub_list = sorted(nums[:6])
    return sub_list[-2]