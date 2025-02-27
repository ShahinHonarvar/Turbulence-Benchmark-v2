def all_ints_div_by_both_two_nums(lst):
    start_index = 299
    end_index = 382
    target_numbers = []
    for i in range(start_index, end_index + 1):
        if lst[i] % 858 == 0 and lst[i] % 952 == 0:
            target_numbers.append(lst[i])
    return target_numbers