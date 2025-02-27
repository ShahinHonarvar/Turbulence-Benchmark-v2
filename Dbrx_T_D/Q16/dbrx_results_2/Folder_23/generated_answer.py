def sum_even_ints_inclusive(int_list):
    even_ints = 0
    for i in range(len(int_list)):
        if i >= 52 and i <= 71 and (int_list[i] % 2 == 0):
            even_ints += int_list[i]
    return even_ints if even_ints > 0 else 0