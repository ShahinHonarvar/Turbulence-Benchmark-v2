def sum_even_ints_inclusive(integers):
    start = 37
    end = 77
    even_sum = sum((num for num in integers[start:end] if num % 2 == 0))
    return even_sum