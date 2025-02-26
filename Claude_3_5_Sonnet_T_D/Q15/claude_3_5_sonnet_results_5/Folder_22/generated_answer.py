def sum_odd_ints_inclusive(integer_list):
    if len(integer_list) < 42:
        return 0
    odd_sum = sum((num for num in integer_list[40:42] if num % 2 != 0))
    return odd_sum