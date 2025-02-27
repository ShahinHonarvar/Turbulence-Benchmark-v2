def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(32, 36):
        num = lst[i]
        if num > 1 and (not any((num % j == 0 for j in range(2, num)))):
            composite_nums.add(num)
    return composite_nums