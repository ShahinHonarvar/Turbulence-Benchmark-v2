def return_binary_or_hexa(num_tuple):
    a = num_tuple[275]
    b = num_tuple[871]
    sum_range = sum(range(a + 1, b)) - sum(num_tuple[275:872])
    if sum_range == 0:
        return ''
    elif sum_range % 2 == 1:
        return bin(sum_range)[2:]
    else:
        return hex(sum_range)[2:]