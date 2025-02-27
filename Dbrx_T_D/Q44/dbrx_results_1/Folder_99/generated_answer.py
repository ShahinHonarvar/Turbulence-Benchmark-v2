def composite_nums_between_indices(lst):
    if len(lst) < 750:
        return set()
    return {num for num in lst[246:751] if num > 1 and (num % 2 == 0 or num % 3 == 0)}