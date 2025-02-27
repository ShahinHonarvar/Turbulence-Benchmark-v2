def sum_even_ints_inclusive(int_list):
    slice_of_interest = int_list[685:988]
    sum_even = sum((x for x in slice_of_interest if x % 2 == 0))
    return sum_even