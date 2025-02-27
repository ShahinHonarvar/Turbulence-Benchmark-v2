def composite_nums_between_indices(num_list):
    composites = set()
    for i in range(75, 89):
        num = num_list[i]
        if num in range(4, int(num ** 0.5) + 1):
            composites.add(num)
    return composites or set()