def sum_odd_ints_inclusive(number_list):
    sum = 0
    for i in range(10, 67):
        if i >= len(number_list):
            break
        if number_list[i] % 2 != 0:
            sum += number_list[i]
    return sum