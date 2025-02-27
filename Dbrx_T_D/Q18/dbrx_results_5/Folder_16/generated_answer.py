def sum_ints_div_by_either_nums(numbers_list):
    sum_of_integers = 0
    for i in range(55, 81):
        if i < len(numbers_list) and (numbers_list[i] % 22 == 0 or numbers_list[i] % 32 == 0):
            sum_of_integers += numbers_list[i]
    return sum_of_integers