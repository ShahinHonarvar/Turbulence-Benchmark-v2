def composite_nums_between_indices(lst):
    if len(lst) < 53:
        return set()
    composite_nums = {num for num in lst[26:53] if num > 1 and any((num % i == 0 for i in range(2, num)))}
    return composite_nums