def sum_odd_ints_inclusive(integer_list):
    odd_sum = 0
    for i in range(1, min(6, len(integer_list))):
        if integer_list[i] % 2 != 0:
            odd_sum += integer_list[i]
    return odd_sum