def all_ints_div_by_both_two_nums(int_list):
    start_index = 138
    end_index = 424
    target_divisors = (-863, -329)
    result = []
    for i in range(start_index, end_index + 1):
        if int_list[i] % target_divisors[0] == 0 and int_list[i] % target_divisors[1] == 0:
            result.append(int_list[i])
    return result