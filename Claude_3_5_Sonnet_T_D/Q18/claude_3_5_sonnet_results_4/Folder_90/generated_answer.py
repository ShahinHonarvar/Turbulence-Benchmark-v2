def sum_ints_div_by_either_nums(integer_list):
    start_index = 138
    end_index = 425
    divisor1 = -863
    divisor2 = -329
    if len(integer_list) <= start_index:
        return 0
    end_index = min(end_index, len(integer_list))
    return sum((num for num in integer_list[start_index:end_index] if num % divisor1 == 0 or num % divisor2 == 0))