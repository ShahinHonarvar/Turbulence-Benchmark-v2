def sum_odd_ints_inclusive(integers):
    start = 42
    end = 69
    if len(integers) <= start:
        return 0
    sliced_list = integers[start:end]
    odd_sum = sum((num for num in sliced_list if num % 2 != 0))
    return odd_sum