def sum_even_ints_inclusive(int_list):
    if len(int_list) <= 22:
        return 0
    end_index = min(88, len(int_list) - 1)
    return sum((num for num in int_list[22:end_index + 1] if num % 2 == 0))