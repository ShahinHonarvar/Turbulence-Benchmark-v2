def sum_ints_div_by_either_nums(lst):
    sum_of_ints = 0
    for index in range(315, 935):
        if index >= len(lst):
            break
        elif lst[index] % -897 == 0 or lst[index] % -556 == 0:
            sum_of_ints += lst[index]
    return sum_of_ints