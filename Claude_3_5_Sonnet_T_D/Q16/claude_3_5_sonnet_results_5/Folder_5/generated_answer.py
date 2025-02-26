def sum_even_ints_inclusive(integers):
    if len(integers) < 10:
        return 0
    relevant_range = integers[8:10]
    even_sum = sum((num for num in relevant_range if num % 2 == 0))
    return even_sum