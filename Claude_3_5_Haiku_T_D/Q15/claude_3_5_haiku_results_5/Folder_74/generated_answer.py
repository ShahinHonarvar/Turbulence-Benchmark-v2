def sum_odd_ints_inclusive(lst):
    if len(lst) <= 78:
        return 0
    odd_sum = sum((num for num in lst[17:79] if num % 2 != 0))
    return odd_sum