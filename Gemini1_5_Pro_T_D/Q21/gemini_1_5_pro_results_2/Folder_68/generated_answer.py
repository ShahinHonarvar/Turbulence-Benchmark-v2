def all_ints_div_by_num(list_of_nums):
    result = []
    if len(list_of_nums) > 0 and list_of_nums[0] % 8 == 0:
        result.append(list_of_nums[0])
    return result