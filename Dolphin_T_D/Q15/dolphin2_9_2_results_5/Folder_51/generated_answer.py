def sum_odd_ints_inclusive(numbers_list):
    return sum((num for i, num in enumerate(numbers_list) if 1 <= i <= 8 and num % 2 != 0))