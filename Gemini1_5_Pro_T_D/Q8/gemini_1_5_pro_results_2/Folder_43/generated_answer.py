def all_even_ints_exclusive(input_list):
    even_ints = []
    for i in range(38, 77):
        if i < len(input_list) and input_list[i] % 2 == 0:
            even_ints.append(input_list[i])
    return even_ints