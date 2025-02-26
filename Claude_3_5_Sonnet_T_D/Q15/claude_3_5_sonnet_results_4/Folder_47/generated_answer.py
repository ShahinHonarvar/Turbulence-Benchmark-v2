def sum_odd_ints_inclusive(int_list):
    start_index = 37
    end_index = 77
    if len(int_list) <= start_index:
        return 0
    relevant_slice = int_list[start_index:end_index]
    odd_sum = sum((num for num in relevant_slice if num % 2 != 0))
    return odd_sum