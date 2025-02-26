def sum_even_ints_inclusive(int_list):
    if len(int_list) <= 70:
        return 0
    end = min(201, len(int_list))
    return sum((num for num in int_list[70:end] if num % 2 == 0))