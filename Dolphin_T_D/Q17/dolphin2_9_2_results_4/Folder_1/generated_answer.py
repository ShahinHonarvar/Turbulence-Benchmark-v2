def all_ints_div_by_both_two_nums(input_list):
    result = [num for num in input_list[10:28] if num % -61 == 0 and num % -64 == 0]
    if not result:
        result = []
    return result