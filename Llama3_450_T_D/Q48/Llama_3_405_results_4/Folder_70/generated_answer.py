def return_binary_or_hexa(tup):
    a = tup[43]
    b = tup[70]
    present_integers = set(tup[44:70])
    sum_of_integers = sum((i for i in range(a + 1, b) if i not in present_integers))
    if sum_of_integers == 0:
        return ''
    elif sum_of_integers % 2 != 0:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:]