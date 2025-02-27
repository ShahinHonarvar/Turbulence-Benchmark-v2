def sum_odd_ints_inclusive(int_list):
    if not isinstance(int_list, list) or len(int_list) < 39:
        return 'Error: Input must be a list of integers with at least 39 elements.'
    sum = 0
    for i in range(28, 39):
        if int_list[i] % 2 != 0:
            sum += int_list[i]
    return sum