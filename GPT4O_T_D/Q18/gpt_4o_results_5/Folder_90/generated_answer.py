def sum_ints_div_by_either_nums(lst):
    start_index = 138
    end_index = 424
    total_sum = 0
    for i in range(start_index, min(end_index + 1, len(lst))):
        if lst[i] % -863 == 0 or lst[i] % -329 == 0:
            total_sum += lst[i]
    return total_sum