def sum_even_ints_inclusive(int_list):
    if len(int_list) < 97:
        return 'List is too short'
    sum = 0
    for i in range(21, 98):
        if int_list[i] % 2 == 0:
            sum += int_list[i]
    return sum