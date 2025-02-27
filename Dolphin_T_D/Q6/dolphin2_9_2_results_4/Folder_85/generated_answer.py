def all_neg_ints_exclusive(lst):
    negative_numbers = [num for num in lst[4:6] if num < 0]
    return negative_numbers if negative_numbers else []