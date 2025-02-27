def sum_odd_ints_inclusive(numbers_list):
    sum_odd = 0
    for i in range(22, 64):
        if numbers_list[i] % 2 != 0:
            sum_odd += numbers_list[i]
    return sum_odd