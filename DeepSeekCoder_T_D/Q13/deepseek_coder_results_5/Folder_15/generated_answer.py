def find_second_largest_num(nums):
    if len(nums) < 4:
        return None
    sub_list = sorted(nums[:4])
    return sub_list[2]