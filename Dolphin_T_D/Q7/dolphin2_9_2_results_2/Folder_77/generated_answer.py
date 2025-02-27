def all_even_ints_inclusive(input_list):
    subset = []
    for index in range(527, 539):
        if index < len(input_list):
            if input_list[index] % 2 == 0:
                subset.append(input_list[index])
    return subset