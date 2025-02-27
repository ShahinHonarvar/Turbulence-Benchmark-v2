def sum_even_ints_inclusive(lst):
    return sum((lst[i] for i in range(310, 371) if i % 2 == 0))