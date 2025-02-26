def sum_even_ints_inclusive(integers):
    start_index = 55
    end_index = 99
    if len(integers) <= start_index:
        return 0
    sliced_list = integers[start_index:end_index]
    even_sum = sum((num for num in sliced_list if num % 2 == 0))
    return even_sum