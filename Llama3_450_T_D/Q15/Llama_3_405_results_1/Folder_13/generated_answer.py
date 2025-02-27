def sum_odd_ints_inclusive(integers):
    return sum((num for i, num in enumerate(integers[25:88]) if num % 2 != 0))