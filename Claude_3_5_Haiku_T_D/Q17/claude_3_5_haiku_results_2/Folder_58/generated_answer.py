def all_ints_div_by_both_two_nums(input_list):
    result = []
    for num in input_list[240:902]:
        if num % 546 == 0 and num % 709 == 0:
            result.append(num)
    return result