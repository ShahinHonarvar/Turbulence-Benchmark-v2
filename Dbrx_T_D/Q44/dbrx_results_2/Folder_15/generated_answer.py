def composite_nums_between_indices(lst):
    if len(lst) < 4:
        return {}
    else:
        return {num for num in lst[:4] if num > 1 and (not any((num % i == 0 for i in range(2, num))))}