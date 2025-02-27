def all_ints_div_by_num(list_of_nums):
    result = []
    if len(list_of_nums) > 0:
        for i in list_of_nums[:1]:
            if i % 9 == 0:
                result.append(i)
    return result