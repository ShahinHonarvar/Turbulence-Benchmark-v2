def sum_odd_ints_inclusive(integer_list):
    start_index = 13
    end_index = 69
    if len(integer_list) <= start_index:
        return 0
    odd_sum = sum((num for num in integer_list[start_index:end_index] if num % 2 != 0))
    return odd_sum