def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in lst[45:92]:
        if i % 67 == 0 or i % 15 == 0:
            total += i
    return total