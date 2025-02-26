def sum_even_ints_inclusive(integer_list):
    start_index = 30
    end_index = 88
    if len(integer_list) <= start_index:
        return 0
    sliced_list = integer_list[start_index:end_index]
    even_sum = sum((num for num in sliced_list if num % 2 == 0))
    return even_sum