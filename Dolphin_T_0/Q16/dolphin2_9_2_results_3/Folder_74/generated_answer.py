def sum_even_ints_inclusive(lst):
    return sum((lst[i] for i in range(17, 79) if i < len(lst) and lst[i] % 2 == 0))