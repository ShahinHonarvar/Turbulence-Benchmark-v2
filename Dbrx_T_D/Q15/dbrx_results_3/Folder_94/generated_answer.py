def sum_odd_ints_inclusive(integer_list):
    sum = 0
    for i in range(28, 41):
        if i >= len(integer_list):
            break
        if integer_list[i] % 2 != 0:
            sum += integer_list[i]
    return sum