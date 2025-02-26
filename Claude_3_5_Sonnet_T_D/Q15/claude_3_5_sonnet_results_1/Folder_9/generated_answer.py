def sum_odd_ints_inclusive(int_list):
    start = 70
    end = 201
    return sum((num for num in int_list[start:end] if num % 2 != 0))