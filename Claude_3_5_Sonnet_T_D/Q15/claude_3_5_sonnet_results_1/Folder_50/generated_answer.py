def sum_odd_ints_inclusive(integer_list):
    if len(integer_list) < 85:
        return 0
    return sum((num for num in integer_list[70:85] if num % 2 != 0))