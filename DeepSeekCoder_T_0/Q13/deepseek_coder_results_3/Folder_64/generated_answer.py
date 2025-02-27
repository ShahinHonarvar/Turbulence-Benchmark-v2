def find_second_largest_num(nums):
    if len(nums) < 5:
        return None
    sub_list = sorted(nums[:5])
    return sub_list[-2]