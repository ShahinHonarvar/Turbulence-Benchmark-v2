def sum_even_ints_inclusive(int_list):
    sum_of_even_ints = 0
    for i in range(33, 37):
        if i < len(int_list) and int_list[i] % 2 == 0:
            sum_of_even_ints += int_list[i]
    return sum_of_even_ints