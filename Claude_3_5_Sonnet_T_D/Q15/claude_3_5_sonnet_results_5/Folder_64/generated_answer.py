def sum_odd_ints_inclusive(integer_list):
    total = 0
    for i in range(min(5, len(integer_list))):
        if integer_list[i] % 2 != 0:
            total += integer_list[i]
    return total