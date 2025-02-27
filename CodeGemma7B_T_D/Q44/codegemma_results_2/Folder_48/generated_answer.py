def composite_nums_between_indices(input_list):
    composites = set()
    for i in range(661, 925):
        if input_list[i] != 1:
            for j in range(2, input_list[i] + 1):
                if input_list[i] % j == 0 and i > j:
                    composites.add(input_list[i])
    return composites