def sum_odd_ints_inclusive(integer_list):
    if len(integer_list) < 47:
        return 0
    return sum((num for num in integer_list[36:47] if num % 2 != 0))