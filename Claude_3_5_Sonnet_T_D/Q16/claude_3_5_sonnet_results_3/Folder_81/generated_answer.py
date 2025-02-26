def sum_even_ints_inclusive(int_list):
    if len(int_list) <= 10:
        return 0
    end_index = min(101, len(int_list))
    return sum((num for num in int_list[10:end_index] if num % 2 == 0))