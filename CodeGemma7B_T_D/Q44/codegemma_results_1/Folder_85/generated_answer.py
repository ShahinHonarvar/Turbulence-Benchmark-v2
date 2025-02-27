def composite_nums_between_indices(num_list):
    composites = set()
    for num in num_list[3:6]:
        if 1 < num < max(num_list):
            for factor in range(2, num):
                if num % factor == 0:
                    composites.add(num)
    return composites