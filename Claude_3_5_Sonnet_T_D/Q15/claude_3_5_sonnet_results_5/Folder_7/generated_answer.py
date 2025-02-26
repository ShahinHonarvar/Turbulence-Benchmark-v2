def sum_odd_ints_inclusive(int_list):
    start_index = 661
    end_index = 924
    if len(int_list) <= start_index:
        return 0
    end_index = min(end_index, len(int_list) - 1)
    odd_sum = sum((num for num in int_list[start_index:end_index + 1] if num % 2 != 0))
    return odd_sum