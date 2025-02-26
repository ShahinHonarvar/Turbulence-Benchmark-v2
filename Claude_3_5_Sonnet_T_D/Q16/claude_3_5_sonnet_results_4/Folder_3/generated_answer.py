def sum_even_ints_inclusive(integers):
    start = 62
    end = 93
    even_sum = sum((num for num in integers[start:end] if num % 2 == 0))
    return even_sum