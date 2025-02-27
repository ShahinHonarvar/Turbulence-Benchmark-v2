def sum_ints_div_by_either_nums(int_list):
    start_index = 13
    end_index = 18
    if len(int_list) < start_index + 1:
        return 0
    sum_divisible = sum((num for num in int_list[start_index:end_index + 1] if num % 45 == 0 or num % 20 == 0))
    return sum_divisible