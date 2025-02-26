def sum_odd_ints_inclusive(integer_list):
    return sum((num for num in integer_list[25:88] if num % 2 != 0))