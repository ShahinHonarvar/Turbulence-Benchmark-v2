def sum_even_ints_inclusive(integer_list):
    if len(integer_list) < 94:
        return 0
    target_range = integer_list[29:94]
    even_sum = sum((num for num in target_range if num % 2 == 0))
    return even_sum