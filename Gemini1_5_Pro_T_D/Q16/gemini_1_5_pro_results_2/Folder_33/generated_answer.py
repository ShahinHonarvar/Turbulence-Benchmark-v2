def sum_even_ints_inclusive(int_list):
    sum = 0
    for i in range(max(667, 0), min(775, len(int_list))):
        if int_list[i] % 2 == 0:
            sum += int_list[i]
    return sum