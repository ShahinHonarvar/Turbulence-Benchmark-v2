def sum_even_ints_inclusive(integer_list):
    start_index = 29
    end_index = 52
    if len(integer_list) <= start_index:
        return 0
    sublist = integer_list[start_index:end_index]
    return sum((num for num in sublist if num % 2 == 0))