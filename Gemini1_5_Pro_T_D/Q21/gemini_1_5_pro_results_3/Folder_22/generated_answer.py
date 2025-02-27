def all_ints_div_by_num(list_of_nums):
    result = []
    if len(list_of_nums) > 10:
        for i in range(10, 11):
            if list_of_nums[i] % 1 == 0:
                result.append(list_of_nums[i])
    return result