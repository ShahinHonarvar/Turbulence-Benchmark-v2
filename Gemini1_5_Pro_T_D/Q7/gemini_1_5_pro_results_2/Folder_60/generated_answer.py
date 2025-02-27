def all_even_ints_inclusive(int_list):
    even_ints = []
    for i in range(max(0, len(int_list) - (85 - 75) - 1)):
        if 75 <= i <= 85 and int_list[i] % 2 == 0:
            even_ints.append(int_list[i])
    return even_ints