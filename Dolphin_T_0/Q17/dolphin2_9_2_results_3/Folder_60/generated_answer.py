def all_ints_div_by_both_two_nums(lst):
    divisible_numbers = []
    for i in range(10, 80):
        if i in lst and i % -74 == 0 and (i % -58 == 0):
            divisible_numbers.append(i)
    return divisible_numbers