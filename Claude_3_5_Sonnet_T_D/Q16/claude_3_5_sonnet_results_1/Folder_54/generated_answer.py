def sum_even_ints_inclusive(integers):
    start = 34
    end = 56
    return sum((num for num in integers[start:end] if num % 2 == 0))