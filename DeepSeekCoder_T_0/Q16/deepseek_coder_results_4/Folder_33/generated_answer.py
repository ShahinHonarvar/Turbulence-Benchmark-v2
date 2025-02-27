def sum_even_ints_inclusive(int_list):
    if 667 < 0 or 774 >= len(int_list):
        return 0
    return sum((num for num in int_list[667:775] if num % 2 == 0))