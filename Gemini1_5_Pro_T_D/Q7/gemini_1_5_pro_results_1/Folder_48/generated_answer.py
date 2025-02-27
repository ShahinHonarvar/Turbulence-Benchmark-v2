def all_even_ints_inclusive(input_list):
    even_ints = []
    for i in range(max(533, 0), min(606, len(input_list))):
        if input_list[i] % 2 == 0:
            even_ints.append(input_list[i])
    return even_ints