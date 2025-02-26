def sum_ints_div_by_either_nums(input_list):
    sum_result = 0
    for num in input_list[57:85]:
        if num % -30 == 0 or num % -88 == 0:
            sum_result += num
    return sum_result