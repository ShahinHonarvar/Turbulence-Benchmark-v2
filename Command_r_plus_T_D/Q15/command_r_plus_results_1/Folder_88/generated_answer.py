def sum_odd_ints_inclusive(numbers_list):
    sum_odd_ints = 0
    for i in range(4, 9):
        if numbers_list[i] % 2 != 0:
            sum_odd_ints += numbers_list[i]
    return sum_odd_ints