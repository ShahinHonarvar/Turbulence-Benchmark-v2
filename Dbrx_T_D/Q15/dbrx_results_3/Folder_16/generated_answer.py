def sum_odd_ints_inclusive(integer_list):
    sum = 0
    for i in range(min(33, len(integer_list)), min(37, len(integer_list))):
        if integer_list[i] % 2 != 0:
            sum += integer_list[i]
    return sum