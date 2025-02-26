def sum_even_ints_inclusive(int_list):
    if len(int_list) < 95:
        return 0
    total = 0
    for num in int_list[75:95]:
        if num % 2 == 0:
            total += num
    return total