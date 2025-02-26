def sum_odd_ints_inclusive(integer_list):
    start_index = 527
    end_index = 539
    if len(integer_list) <= start_index:
        return 0
    sliced_list = integer_list[start_index:end_index]
    odd_sum = sum((num for num in sliced_list if num % 2 != 0))
    return odd_sum