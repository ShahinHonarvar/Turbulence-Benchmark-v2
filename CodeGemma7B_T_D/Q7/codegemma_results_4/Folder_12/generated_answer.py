def all_even_ints_inclusive(int_list):
    even_numbers = []
    for i in range(14, 65):
        if int_list[i] % 2 == 0:
            even_numbers.append(int_list[i])
    return even_numbers