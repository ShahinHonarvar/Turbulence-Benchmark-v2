def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 605:
        return 'Input list is too short.'
    sum = 0
    for i in range(533, 606):
        if int_list[i] % 2 != 0:
            sum += int_list[i]
    return sum