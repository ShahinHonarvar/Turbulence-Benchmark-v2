def sum_odd_ints_inclusive(lst):
    in_range = lst[6:7]
    odd_sum = 0
    for num in in_range:
        if num % 2 != 0:
            odd_sum += num
    return odd_sum