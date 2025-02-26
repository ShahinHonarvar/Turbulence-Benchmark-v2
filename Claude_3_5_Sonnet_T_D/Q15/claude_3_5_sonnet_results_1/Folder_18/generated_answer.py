def sum_odd_ints_inclusive(integer_list):
    start_index = 35
    end_index = 50
    if len(integer_list) <= start_index:
        return 0
    range_to_sum = integer_list[start_index:end_index]
    odd_sum = sum((num for num in range_to_sum if num % 2 != 0))
    return odd_sum