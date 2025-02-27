def all_even_ints_inclusive(ints):
    even_ints = []
    for i in range(56, 83):
        if i in range(len(ints)):
            if ints[i] % 2 == 0:
                even_ints.append(ints[i])
    return even_ints