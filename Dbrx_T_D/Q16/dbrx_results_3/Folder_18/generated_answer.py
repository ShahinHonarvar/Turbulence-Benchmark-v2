def sum_even_ints_inclusive(my_list):
    if len(my_list) < 50:
        return 0
    sum = 0
    for i in range(35, 50):
        if my_list[i] % 2 == 0:
            sum += my_list[i]
    return sum