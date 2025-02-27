def composite_nums_between_indices(lst):
    composite_set = set()
    for i in range(29, 94):
        num = lst[i]
        if num > 1 and (not num & 1) and (num % 3 != 0):
            composite_set.add(num)
        elif num > 1 and num % 5 != 0 and (num % 7 != 0):
            composite_set.add(num)
    return composite_set