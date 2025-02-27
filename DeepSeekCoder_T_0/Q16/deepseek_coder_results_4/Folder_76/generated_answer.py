def sum_even_ints_inclusive(int_list):
    if 686 <= len(int_list) - 1 < 987:
        return sum((x for x in int_list[686:988] if x % 2 == 0))
    elif len(int_list) - 1 >= 987:
        return sum((x for x in int_list[686:988] if x % 2 == 0))
    else:
        return 0