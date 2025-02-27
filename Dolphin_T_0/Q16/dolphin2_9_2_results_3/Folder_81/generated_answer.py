def sum_even_ints_inclusive(integers_list):
    total = 0
    for i in range(10, 101):
        if i < len(integers_list) and integers_list[i] % 2 == 0:
            total += integers_list[i]
    return total