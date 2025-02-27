def sum_even_ints_inclusive(lst):
    even_sum = sum([i for i in lst[32:36] if i % 2 == 0])
    return even_sum if even_sum else 0