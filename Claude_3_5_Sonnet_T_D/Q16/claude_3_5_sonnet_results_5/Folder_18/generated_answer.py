def sum_even_ints_inclusive(integers):
    slice = integers[35:50]
    return sum((num for num in slice if num % 2 == 0))