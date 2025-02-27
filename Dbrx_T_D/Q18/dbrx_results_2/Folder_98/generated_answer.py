def sum_ints_div_by_either_nums(int_list):
    total = 0
    for i, num in enumerate(int_list[:6]):
        if i >= 5:
            break
        if num % -1 == 0 or num % 13 == 0:
            total += num
    return total