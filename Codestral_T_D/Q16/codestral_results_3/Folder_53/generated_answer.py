def sum_even_ints_inclusive(lst):
    return sum([num for i, num in enumerate(lst[111:112]) if i % 2 == 0 and num % 2 == 0])