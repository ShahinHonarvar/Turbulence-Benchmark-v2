def sum_even_ints_inclusive(int_list):
    if len(int_list) > 111:
        return sum((x for x in int_list[111:112] if x % 2 == 0))
    return 0