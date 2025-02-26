def sum_odd_ints_inclusive(integer_list):
    if len(integer_list) < 10:
        return 0
    return sum((num for num in integer_list[8:10] if num % 2 != 0))