def composite_nums_between_indices(number_list):
    composites = set()
    for i in range(0, 5):
        if number_list[i] % 2 == 0 or (number_list[i] % 3 == 0 and number_list[i] != 3) or number_list[i] % 5 == 0 or (number_list[i] % 7 == 0 and number_list[i] != 7):
            composites.add(number_list[i])
    return composites