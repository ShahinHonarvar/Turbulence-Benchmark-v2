def sum_even_ints_inclusive(int_list):
    sum = 0
    for i in range(75, 86):
        if i in range(len(int_list)) and int_list[i] % 2 == 0:
            sum += int_list[i]
    return sum