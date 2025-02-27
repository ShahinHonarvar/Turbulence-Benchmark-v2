def all_ints_div_by_both_two_nums(input_list):
    result_list = []
    for num in input_list[0:10]:
        if num % 6 == 0 and num % -3 == 0:
            result_list.append(num)
    return result_list