def sum_ints_div_by_either_nums(int_list):
    total = 0
    for num in int_list[20:94]:
        if num % -92 == 0 or num % -50 == 0:
            total += num
    return total