def sum_odd_ints_inclusive(int_list):
    sum = 0
    for n in int_list[14:65]:
        if n % 2 != 0:
            sum += n
    if sum == 0:
        return 0
    return sum