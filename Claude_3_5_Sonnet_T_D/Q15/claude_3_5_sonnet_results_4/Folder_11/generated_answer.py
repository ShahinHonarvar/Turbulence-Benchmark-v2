def sum_odd_ints_inclusive(integer_list):
    if len(integer_list) < 52:
        return 0
    slice_to_sum = integer_list[37:52]
    odd_sum = sum((num for num in slice_to_sum if num % 2 != 0))
    return odd_sum