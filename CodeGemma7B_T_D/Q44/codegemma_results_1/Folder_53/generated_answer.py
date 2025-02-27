def composite_nums_between_indices(num_list):
    composites = set()
    for num in num_list[222:223]:
        for factor in range(2, int(num ** 0.5) + 1):
            if num % factor == 0:
                composites.add(num)
                break
    return composites