def sum_even_ints_inclusive(num_list):
    even_nums = 0
    for num in num_list[533:606]:
        if num % 2 == 0:
            even_nums += num
    if even_nums == 0:
        return 0
    return even_nums