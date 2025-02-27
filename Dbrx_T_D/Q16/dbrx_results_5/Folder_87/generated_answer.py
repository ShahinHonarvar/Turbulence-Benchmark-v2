def sum_even_ints_inclusive(my_list):
    start, end = (36, 46)
    my_slice = my_list[start:end + 1]
    even_sum = sum((x for x in my_slice if x % 2 == 0))
    return even_sum if even_sum != 0 else 0