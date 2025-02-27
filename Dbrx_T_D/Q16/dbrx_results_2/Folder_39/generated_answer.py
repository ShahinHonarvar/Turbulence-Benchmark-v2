def sum_even_ints_inclusive(int_list):
    even_sum = 0
    for i in range(len(int_list)):
        if i < 20 or i > 30:
            continue
        if int_list[i] % 2 == 0:
            even_sum += int_list[i]
    if even_sum == 0:
        return 0
    else:
        return even_sum