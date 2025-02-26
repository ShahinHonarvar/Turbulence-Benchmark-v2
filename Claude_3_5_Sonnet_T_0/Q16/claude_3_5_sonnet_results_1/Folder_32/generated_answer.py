def sum_even_ints_inclusive(integer_list):
    if len(integer_list) < 98:
        return 0
    total = 0
    for num in integer_list[21:98]:
        if num % 2 == 0:
            total += num
    return total