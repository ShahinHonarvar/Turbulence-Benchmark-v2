def sum_even_ints_inclusive(int_list):
    total_sum = 0
    for i in range(37, 77):
        if i >= 37 and i <= 76:
            if int_list[i] % 2 == 0:
                total_sum += int_list[i]
    if total_sum == 0:
        return 0
    else:
        return total_sum