def composite_nums_between_indices(lst):
    composites = set()
    for num in lst:
        if 2 <= lst.index(num) <= 2:
            for i in range(2, num):
                if num % i == 0:
                    composites.add(num)
                    break
    return composites