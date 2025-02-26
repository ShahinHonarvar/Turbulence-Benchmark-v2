def sum_odd_ints_inclusive(integers):
    start = 59
    end = 98
    if len(integers) <= start:
        return 0
    subset = integers[start:end]
    odd_sum = sum((num for num in subset if num % 2 != 0))
    return odd_sum