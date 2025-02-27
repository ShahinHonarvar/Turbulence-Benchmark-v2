def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    sub_list = nums[:2]
    sub_list.sort(reverse=True)
    return sub_list[1]