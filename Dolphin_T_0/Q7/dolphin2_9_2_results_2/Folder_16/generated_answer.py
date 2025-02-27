def all_even_ints_inclusive(l):
    output = []
    for i in range(33, 37):
        if i < len(l):
            if l[i] % 2 == 0:
                output.append(l[i])
    return output