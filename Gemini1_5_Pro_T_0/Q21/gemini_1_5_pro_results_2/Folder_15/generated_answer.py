def all_ints_div_by_num(list_of_nums):
    result = []
    if len(list_of_nums) > 0:
        for i in range(0, 1):
            if list_of_nums[i] % 3 == 0:
                result.append(list_of_nums[i])
    return result