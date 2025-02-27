def sum_even_ints_inclusive(int_list):
    sum = 0
    for i in range(29, 80):
        if i < 0 or i >= len(int_list):
            continue
        if int_list[i] % 2 == 0:
            sum += int_list[i]
    return sum