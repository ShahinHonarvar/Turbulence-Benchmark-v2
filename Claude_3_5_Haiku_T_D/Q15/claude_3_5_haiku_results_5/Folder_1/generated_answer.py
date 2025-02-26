def sum_odd_ints_inclusive(lst):
    if len(lst) <= 72:
        return 0
    odd_sum = sum((num for num in lst[31:73] if num % 2 != 0))
    return odd_sum