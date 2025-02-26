def sum_even_ints_inclusive(integers):
    if len(integers) < 86:
        return 0
    target_range = integers[75:86]
    even_sum = sum((num for num in target_range if num % 2 == 0))
    return even_sum