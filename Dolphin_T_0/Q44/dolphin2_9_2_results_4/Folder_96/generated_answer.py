def composite_nums_between_indices(lst):
    set_of_composite_nums = set()
    for i in range(60, 201):
        if lst[i] > 1:
            for j in range(2, lst[i]):
                if lst[i] % j == 0:
                    set_of_composite_nums.add(lst[i])
                    break
    return set_of_composite_nums