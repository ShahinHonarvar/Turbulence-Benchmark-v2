def sum_odd_ints_inclusive(int_list):
    if 56 <= len(int_list) <= 57:
        odd_sum = sum((num for num in int_list[56:58] if num % 2 != 0))
        return odd_sum
    else:
        return 0