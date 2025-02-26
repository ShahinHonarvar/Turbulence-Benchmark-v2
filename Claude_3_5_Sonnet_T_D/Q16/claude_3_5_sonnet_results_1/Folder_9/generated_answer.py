def sum_even_ints_inclusive(integer_list):
    start_index = 70
    end_index = 200
    return sum((num for num in integer_list[start_index:end_index + 1] if num % 2 == 0))