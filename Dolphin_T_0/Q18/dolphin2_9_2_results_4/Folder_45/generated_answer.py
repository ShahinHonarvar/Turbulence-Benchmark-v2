def sum_ints_div_by_either_nums(ints):
    result = 0
    for num in ints[30:201]:
        if num % -115 == 0 or num % 115 == 0:
            result += num
    return result if result != 0 else 0