def sum_ints_div_by_either_nums(integer_list):
    if len(integer_list) <= 7:
        return 0
    return sum((num for num in integer_list[7:8] if num % 5 == 0 or num % 7 == 0))