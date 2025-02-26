def sum_even_ints_inclusive(integers):
    return sum((num for num in integers[1:9] if num % 2 == 0))