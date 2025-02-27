def sum_even_ints_inclusive(int_list):
    if 25 > len(int_list) - 1 or 87 > len(int_list) - 1:
        return 0
    return sum((num for num in int_list[25:88] if num % 2 == 0))