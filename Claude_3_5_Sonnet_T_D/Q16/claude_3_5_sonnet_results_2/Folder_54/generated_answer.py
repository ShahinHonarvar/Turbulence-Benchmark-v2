def sum_even_ints_inclusive(int_list):
    if len(int_list) < 56:
        return 0
    even_sum = 0
    for num in int_list[34:56]:
        if num % 2 == 0:
            even_sum += num
    return even_sum