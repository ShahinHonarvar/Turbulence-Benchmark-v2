def all_even_ints_inclusive(input_list):
    even_ints = []
    for i in range(max(686, 0), min(len(input_list), 988)):
        if input_list[i] % 2 == 0:
            even_ints.append(input_list[i])
    return even_ints