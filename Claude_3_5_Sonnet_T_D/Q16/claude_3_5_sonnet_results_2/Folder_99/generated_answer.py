def sum_even_ints_inclusive(integers):
    start = 310
    end = 371
    return sum((num for num in integers[start:end] if num % 2 == 0))