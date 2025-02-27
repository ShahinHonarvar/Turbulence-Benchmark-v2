def sum_odd_ints_inclusive(integer_list):
    sum = 0
    for i in range(527, 539):
        if i >= 0 and i < len(integer_list):
            if integer_list[i] % 2 != 0:
                sum += integer_list[i]
    return sum