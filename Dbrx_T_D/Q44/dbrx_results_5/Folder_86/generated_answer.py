def composite_nums_between_indices(lst):
    return {num for num in lst[43:87] if num > 1 and (not all((num % i for i in range(2, num))))} if len(lst) >= 87 else {}