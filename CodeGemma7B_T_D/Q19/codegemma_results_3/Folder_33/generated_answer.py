def all_ints_not_div_by_num(numbers):
    new_list = []
    for i in range(104, 574):
        if numbers[i] % -514 != 0:
            new_list.append(numbers[i])
    return new_list