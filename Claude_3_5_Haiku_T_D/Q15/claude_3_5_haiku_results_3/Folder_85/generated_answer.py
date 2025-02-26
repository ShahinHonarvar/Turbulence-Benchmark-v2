def sum_odd_ints_inclusive(lst):
    if len(lst) < 9:
        return 0
    odd_sum = sum((num for num in lst[6:9] if num % 2 != 0))
    return odd_sum