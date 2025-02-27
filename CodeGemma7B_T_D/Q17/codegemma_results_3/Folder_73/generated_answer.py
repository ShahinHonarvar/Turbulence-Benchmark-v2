def all_ints_div_by_both_two_nums(list_nums):
    temp_answer = list()
    for i in list_nums[81:87]:
        if i % 33 == 0 and i % 62 == 0:
            temp_answer.append(i)
    return temp_answer if temp_answer else []