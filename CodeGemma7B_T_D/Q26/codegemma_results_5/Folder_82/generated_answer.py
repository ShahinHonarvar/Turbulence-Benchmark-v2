def sum_in_range(list_int):
    sum_list = 0
    for i in list_int:
        if i >= 5 and i <= 8:
            sum_list += i
    return sum_list if sum_list else 0