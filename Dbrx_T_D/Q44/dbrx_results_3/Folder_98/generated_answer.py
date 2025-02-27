def composite_nums_between_indices(lst):
    composite_nums = {num for num in lst[0:7] if num > 1 and (not all((num % i for i in range(2, num))))}
    return composite_nums