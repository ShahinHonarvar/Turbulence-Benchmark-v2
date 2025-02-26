def sum_even_ints_inclusive(integers):
    start = 262
    end = 747
    return sum((num for num in integers[start:end] if num % 2 == 0))