def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) < 11:
        return None
    sub_list = nums[:11]
    sub_list.sort()
    return sub_list[-2]