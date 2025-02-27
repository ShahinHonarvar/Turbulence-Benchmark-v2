def sum_even_ints_inclusive(int_list):
    sum = 0
    for i in range(6, 9):
        if i in range(len(int_list)):
            if int_list[i] % 2 == 0:
                sum += int_list[i]
    return 0 if len(int_list) < 9 or sum == 0 else sum