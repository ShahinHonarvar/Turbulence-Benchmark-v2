def sum_even_ints_inclusive(integers):
    start = 209
    end = 557
    return sum((num for num in integers[start:end] if num % 2 == 0))