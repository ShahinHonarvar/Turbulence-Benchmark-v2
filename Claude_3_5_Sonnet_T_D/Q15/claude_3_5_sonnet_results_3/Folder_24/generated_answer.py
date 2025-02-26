def sum_odd_ints_inclusive(integers):
    start = 74
    end = 96
    if len(integers) <= start:
        return 0
    relevant_slice = integers[start:end]
    odd_sum = sum((num for num in relevant_slice if num % 2 != 0))
    return odd_sum