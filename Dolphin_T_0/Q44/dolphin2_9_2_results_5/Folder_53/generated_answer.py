def composite_nums_between_indices(num_list):
    composition_set = set()
    for num in num_list[222:223]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    composition_set.add(num)
                    break
    return composition_set