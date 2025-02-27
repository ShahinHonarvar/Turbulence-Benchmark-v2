def sum_ints_div_by_either_nums(input_list):
    sum = 0
    for number in input_list[41:57]:
        if number % 82 == 0 or number % 90 == 0:
            sum += number
    return sum