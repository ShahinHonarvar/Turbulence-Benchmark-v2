def sum_odd_ints_inclusive(num_list):
    if not any((num % 2 for num in num_list[25:60])):
        return 0
    return sum((num for num in num_list[25:60] if num % 2))