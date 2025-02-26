def sum_odd_ints_inclusive(integer_list):
    start = 28
    end = 39
    odd_sum = sum((num for num in integer_list[start:end] if num % 2 != 0))
    return odd_sum