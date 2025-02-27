def composite_nums_between_indices(lst):
    if len(lst) < 73:
        return set()
    composite_nums = set()
    for i in range(31, 73):
        num = lst[i]
        if num > 1 and (not any((num % j == 0 for j in range(2, num)))):
            composite_nums.add(num)
    return composite_nums