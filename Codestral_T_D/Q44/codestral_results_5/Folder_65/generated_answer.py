def composite_nums_between_indices(lst):
    composites = set()
    for i in range(82, 87):
        num = lst[i]
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    composites.add(num)
                    break
    return composites