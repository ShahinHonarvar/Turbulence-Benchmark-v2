def sum_odd_ints_inclusive(integer_list):
    start = 28
    end = min(33, len(integer_list))
    return sum((num for num in integer_list[start:end] if num % 2 != 0))