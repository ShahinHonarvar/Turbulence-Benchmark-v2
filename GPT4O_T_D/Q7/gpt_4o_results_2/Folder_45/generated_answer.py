def all_even_ints_inclusive(integers):
    subset = integers[30:201]
    return [num for num in subset if num % 2 == 0]