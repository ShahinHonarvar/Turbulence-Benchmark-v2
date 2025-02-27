def all_odd_ints_inclusive(list_in):
    output = []
    for i in range(10, 67):
        if i in range(len(list_in)):
            if list_in[i] % 2 != 0:
                output.append(list_in[i])
    return output