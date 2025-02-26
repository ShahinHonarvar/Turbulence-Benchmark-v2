def all_even_ints_inclusive(int_list):
    start = 50
    end = 201
    return [num for num in int_list[start:end] if num % 2 == 0]