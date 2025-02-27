def all_neg_ints_inclusive(lst):
    if not any((num < 0 for num in lst[13:69])):
        return []
    return [num for num in lst[13:69] if num < 0]