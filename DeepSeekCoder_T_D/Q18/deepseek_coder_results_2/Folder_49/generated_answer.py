def sum_ints_div_by_either_nums(int_list):
    total = 0
    for num in int_list[80:201]:
        if num % 10 == 0 or num % 1000 == 0:
            total += num
    return total