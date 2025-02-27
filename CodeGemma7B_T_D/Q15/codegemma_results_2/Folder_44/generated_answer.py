def sum_odd_ints_inclusive(int_list):
    sum = 0
    for index in range(13, 69):
        if index % 2 != 0 and index in range(13, 69):
            sum += int_list[index]
    if sum == 0:
        return 0
    return sum