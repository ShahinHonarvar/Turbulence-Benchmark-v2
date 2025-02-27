def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(50, 201):
        num = lst[i]
        if num < 2:
            continue
        for j in range(2, num):
            if num % j == 0:
                composite_nums.add(num)
    return composite_nums