def sum_even_ints_inclusive(int_list):
    start = 21
    end = 97
    return sum((x for x in int_list[start:end + 1] if x % 2 == 0))