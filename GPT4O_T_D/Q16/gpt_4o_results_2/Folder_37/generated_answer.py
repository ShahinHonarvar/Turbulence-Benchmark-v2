def sum_even_ints_inclusive(int_list):
    sum_evens = 0
    for i in range(1, 6):
        if i < len(int_list) and int_list[i] % 2 == 0:
            sum_evens += int_list[i]
    return sum_evens