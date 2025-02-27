def sum_even_ints_inclusive(lst):
    even_ints_sum = sum((x for x in lst[37:77] if x % 2 == 0))
    return even_ints_sum if even_ints_sum else 0