def sum_odd_ints_inclusive(integer_list):
    if len(integer_list) < 89:
        return 0
    odd_sum = 0
    for i in range(75, 89):
        if integer_list[i] % 2 != 0:
            odd_sum += integer_list[i]
    return odd_sum