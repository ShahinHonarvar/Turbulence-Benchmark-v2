def return_binary_or_hexa(num_tuple):
    a = num_tuple[70]
    b = num_tuple[98]
    sum_integers = sum((i for i in range(a + 1, b) if i not in num_tuple[70:99]))
    if sum_integers % 2 == 0:
        return hex(sum_integers)[2:]
    else:
        return bin(sum_integers)[2:]