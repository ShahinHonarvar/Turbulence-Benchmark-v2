def sum_even_ints_inclusive(num_list):
    sum = 0
    for i in range(0, min(7, len(num_list))):
        if num_list[i] % 2 == 0:
            sum += num_list[i]
    return sum