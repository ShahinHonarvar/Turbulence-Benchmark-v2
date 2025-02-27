def composite_nums_between_indices(lst):
    composite_numbers = set()
    for i in range(len(lst))[27:56]:
        num = lst[i]
        if num > 1 and (num % 2 == 0 or num % 3 == 0):
            composite_numbers.add(num)
    return composite_numbers