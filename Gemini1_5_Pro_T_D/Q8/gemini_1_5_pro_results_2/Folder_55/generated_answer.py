def all_even_ints_exclusive(list_in):
    output = []
    for i in range(1, min(len(list_in), 10)):
        if list_in[i] % 2 == 0:
            output.append(list_in[i])
    return output