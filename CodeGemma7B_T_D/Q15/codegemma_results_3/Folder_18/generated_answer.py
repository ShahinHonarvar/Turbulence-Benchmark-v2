def sum_odd_ints_inclusive(int_list):
    if not any((num % 2 for num in int_list[35:49])):
        return 0
    return sum((num for num in int_list[35:49] if num % 2 != 0))