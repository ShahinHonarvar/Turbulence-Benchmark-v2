def sum_even_ints_inclusive(int_list):
    sum = 0
    for i in range(max(0, min(len(int_list) - 1, 639)), min(len(int_list), 976)):
        if int_list[i] % 2 == 0:
            sum += int_list[i]
    return sum