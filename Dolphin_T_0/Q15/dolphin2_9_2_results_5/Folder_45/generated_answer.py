def sum_odd_ints_inclusive(list):
    return sum((num for i, num in enumerate(list[30:201]) if num % 2 != 0))