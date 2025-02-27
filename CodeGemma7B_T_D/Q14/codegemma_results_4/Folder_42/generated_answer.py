def find_second_smallest_num(list_nums):
    list_nums2 = sorted(list_nums[21:98])
    if len(list_nums2) < 2:
        return None
    else:
        return list_nums2[1]