def sum_odd_ints_inclusive(num_list):
    return sum((num for num in num_list[0:10] if num % 2 != 0))