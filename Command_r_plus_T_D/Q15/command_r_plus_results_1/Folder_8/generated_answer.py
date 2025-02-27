def sum_odd_ints_inclusive(int_list):
    if len(int_list) > 23:
        odd_sum = sum((num for num in int_list[23:] if num % 2 != 0))
        return odd_sum
    else:
        return 0