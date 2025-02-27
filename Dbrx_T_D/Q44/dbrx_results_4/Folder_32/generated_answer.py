def composite_nums_between_indices(lst):
    if len(lst) < 66:
        return {}
    return {num for num in lst[10:67] if num > 1 and num % 2 == 0 and (num % 3 != 0) or (num % 2 != 0 and num % 3 == 0 and (num % 5 != 0))}