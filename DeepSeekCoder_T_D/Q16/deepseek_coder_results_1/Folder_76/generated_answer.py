def sum_even_ints_inclusive(int_list):
    if 686 <= len(int_list) - 1 < 988:
        return sum((num for num in int_list[686:988] if num % 2 == 0))
    return 0