def sum_odd_ints_inclusive(list_of_ints):
    return sum((num for num in list_of_ints[667:775] if num % 2 != 0))