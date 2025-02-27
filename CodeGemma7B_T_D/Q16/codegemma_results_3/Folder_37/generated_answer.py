def sum_even_ints_inclusive(num_list):
    sum = 0
    for i in range(1, 6):
        if ind % 2 == 0:
            sum += num_list[ind]
    return sum