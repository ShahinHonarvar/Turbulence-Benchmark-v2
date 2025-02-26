def sum_even_ints_inclusive(integers):
    start = 55
    end = 99
    subset = integers[start:end]
    even_sum = sum((num for num in subset if num % 2 == 0))
    return even_sum