def sum_odd_ints_inclusive(numbers_list):
    sum_odd_range = sum((num for num in numbers_list[36:47] if num % 2 != 0))
    return sum_odd_range