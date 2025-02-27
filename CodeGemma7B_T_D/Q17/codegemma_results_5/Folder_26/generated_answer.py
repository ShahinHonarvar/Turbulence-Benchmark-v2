def all_ints_div_by_both_two_nums(some_list):
    result = []
    start_index = 69
    end_index = 70
    for i in range(start_index, end_index + 1):
        if i % 72 == 0 and i % 70 == 0:
            result.append(i)
    return result