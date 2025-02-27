def all_even_ints_inclusive(input_list):
    even_ints = []
    for i in range(70, 85):
        if i >= len(input_list):
            break
        if input_list[i] % 2 == 0:
            even_ints.append(input_list[i])
    return even_ints