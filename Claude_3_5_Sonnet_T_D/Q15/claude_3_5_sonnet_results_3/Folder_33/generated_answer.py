def sum_odd_ints_inclusive(integers):
    start_index = 667
    end_index = 775
    sublist = integers[start_index:end_index]
    odd_sum = sum((num for num in sublist if num % 2 != 0))
    return odd_sum