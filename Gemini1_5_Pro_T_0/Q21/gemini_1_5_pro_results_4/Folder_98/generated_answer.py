def all_ints_div_by_num(list_of_nums):
    result = []
    if len(list_of_nums) > 0:
        if list_of_nums[0] % 6 == 0:
            result.append(list_of_nums[0])
    return result