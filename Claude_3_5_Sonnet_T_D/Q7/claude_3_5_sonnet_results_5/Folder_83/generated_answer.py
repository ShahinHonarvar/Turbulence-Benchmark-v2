def all_even_ints_inclusive(int_list):
    start = min(90, len(int_list))
    end = min(201, len(int_list))
    return [num for num in int_list[start:end] if num % 2 == 0]