def find_second_largest_num(list_nums):
    if len(list_nums) < 2:
        return None
    list_nums.sort()
    return list_nums[36:77][-2] if len(list_nums[36:77]) >= 2 else None