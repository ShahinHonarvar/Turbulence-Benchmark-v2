def sum_even_ints_inclusive(num_list):
    if len(num_list) < 36:
        return 0
    return sum((num for num in num_list[32:36] if num % 2 == 0))