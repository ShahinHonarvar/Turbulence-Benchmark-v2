def sum_odd_ints_inclusive(integer_list):
    if len(integer_list) < 100:
        return 0
    return sum((num for num in integer_list[62:100] if num % 2 != 0))