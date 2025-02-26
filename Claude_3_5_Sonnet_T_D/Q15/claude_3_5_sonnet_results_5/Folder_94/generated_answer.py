def sum_odd_ints_inclusive(integer_list):
    start = 28
    end = 41
    odd_sum = 0
    for i in range(start, end):
        if i < len(integer_list) and integer_list[i] % 2 != 0:
            odd_sum += integer_list[i]
    return odd_sum