def sum_even_ints_inclusive(integer_list):
    if len(integer_list) < 86:
        return 0
    range_sum = 0
    for i in range(75, 86):
        if integer_list[i] % 2 == 0:
            range_sum += integer_list[i]
    return range_sum