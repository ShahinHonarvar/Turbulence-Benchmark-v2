def return_binary_or_hexa(num_tuple):
    a, b = (num_tuple[3], num_tuple[8])
    sum_desired = sum(range(a + 1, b))
    if sum_desired % 2 == 0:
        return hex(sum_desired)[2:].upper()
    else:
        return bin(sum_desired)[2:]