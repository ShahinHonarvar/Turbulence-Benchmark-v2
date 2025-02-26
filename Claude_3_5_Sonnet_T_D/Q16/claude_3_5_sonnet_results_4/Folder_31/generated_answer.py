def sum_even_ints_inclusive(int_list):
    if len(int_list) < 89:
        return 0
    target_range = int_list[75:89]
    even_sum = sum((num for num in target_range if num % 2 == 0))
    return even_sum