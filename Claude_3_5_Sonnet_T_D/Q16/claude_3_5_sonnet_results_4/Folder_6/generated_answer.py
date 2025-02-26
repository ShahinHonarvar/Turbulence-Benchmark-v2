def sum_even_ints_inclusive(int_list):
    if len(int_list) <= 10:
        return 0
    end = min(67, len(int_list))
    return sum((num for num in int_list[10:end] if num % 2 == 0))