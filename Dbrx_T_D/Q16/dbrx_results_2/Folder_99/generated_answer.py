def sum_even_ints_inclusive(int_list):
    start, end = (310, 370)
    if len(int_list) < end:
        return 0
    sum_even = 0
    for i in range(start, end + 1):
        if i < len(int_list) and int_list[i] % 2 == 0:
            sum_even += int_list[i]
    return sum_even