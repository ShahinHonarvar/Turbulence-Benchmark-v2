def sum_even_ints_inclusive(integer_list):
    if len(integer_list) < 40:
        return 0
    even_sum = 0
    for num in integer_list[15:40]:
        if num % 2 == 0:
            even_sum += num
    return even_sum