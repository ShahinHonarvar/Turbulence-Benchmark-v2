def sum_ints_div_by_either_nums(integers):
    result = 0
    for num in integers[11:77]:
        if num % -81 == 0 or num % -94 == 0:
            result += num
    return result