def sum_even_ints_inclusive(int_list):
    sum = 0
    for i in range(len(int_list)):
        if i >= 62 and i <= 78:
            if int_list[i] % 2 == 0:
                sum += int_list[i]
    return sum