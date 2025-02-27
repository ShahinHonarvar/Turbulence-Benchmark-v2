def sum_odd_ints_inclusive(int_list):
    if 75 <= 85 < len(int_list):
        return sum((num for num in int_list[75:86] if num % 2 != 0))
    return 0