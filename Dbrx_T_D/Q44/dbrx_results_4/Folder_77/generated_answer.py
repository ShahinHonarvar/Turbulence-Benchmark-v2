def composite_nums_between_indices(lst):
    composite_numbers = set()
    for i in range(667, 775):
        num = lst[i]
        if num > 1 and (not all((num % j for j in range(2, num)))):
            composite_numbers.add(num)
    return composite_numbers