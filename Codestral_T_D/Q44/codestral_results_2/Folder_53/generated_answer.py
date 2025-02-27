def composite_nums_between_indices(num_list):
    composites = set()
    for i in range(222, 223):
        num = num_list[i]
        for j in range(2, num):
            if num % j == 0:
                composites.add(num)
                break
    return composites