def composite_nums_between_indices(lst):
    composite_nums_set = set()
    for num in lst[20:31]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    composite_nums_set.add(num)
                    break
    return composite_nums_set