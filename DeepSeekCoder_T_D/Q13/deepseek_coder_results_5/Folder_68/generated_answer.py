def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) < 9:
        return None
    sub_list = sorted(nums[:9])
    return sub_list[-2]