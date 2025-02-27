def composite_nums_between_indices(lst):
    return {num for num in lst[91:100] if num > 1 and num % 2 == 0 or (num % 3 == 0 and num != 2 and (num != 3))}