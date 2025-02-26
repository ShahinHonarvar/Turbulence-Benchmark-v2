def sum_ints_div_by_either_nums(integers):
    total = 0
    for num in integers[20:94]:
        if num % -92 == 0 or num % -50 == 0:
            total += num
    return total