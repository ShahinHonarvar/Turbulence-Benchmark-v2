def sum_odd_ints_inclusive(integer_list):
    return sum((num for num in integer_list[1:9] if num % 2 != 0))