def sum_ints_div_by_either_nums(list_of_ints):
    sum_of_numbers = 0
    for i in range(70, 201):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % 3 == 0 or list_of_ints[i] % -300 == 0:
            sum_of_numbers += list_of_ints[i]
    return sum_of_numbers