def sum_odd_ints_inclusive(integer_list):
    start_index = 34
    end_index = 56
    if len(integer_list) <= start_index:
        return 0
    subset = integer_list[start_index:end_index]
    odd_sum = sum((num for num in subset if num % 2 != 0))
    return odd_sum