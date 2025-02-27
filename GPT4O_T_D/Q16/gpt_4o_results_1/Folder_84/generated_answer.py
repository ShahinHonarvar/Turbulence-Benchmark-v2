def sum_even_ints_inclusive(lst):
    if len(lst) < 87:
        return 0
    return sum((num for num in lst[43:87] if num % 2 == 0))