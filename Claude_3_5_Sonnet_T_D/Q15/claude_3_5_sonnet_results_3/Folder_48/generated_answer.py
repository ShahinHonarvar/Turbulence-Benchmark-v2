def sum_odd_ints_inclusive(integer_list):
    start_index = 533
    end_index = 606
    return sum((num for num in integer_list[start_index:end_index] if num % 2 != 0))