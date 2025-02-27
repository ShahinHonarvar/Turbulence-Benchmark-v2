def sum_odd_ints_inclusive(int_list):
    if 533 <= 605 < len(int_list):
        return sum((num for num in int_list[533:606] if num % 2 != 0))
    return 0