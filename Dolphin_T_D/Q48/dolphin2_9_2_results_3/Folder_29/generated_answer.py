def return_binary_or_hexa(num_tuple):
    a = num_tuple[70]
    b = num_tuple[98]
    if all((x in num_tuple for x in range(a + 1, b))):
        return ''
    sum_nums = sum((x for x in range(a + 1, b + 1) if x not in num_tuple[70:99]))
    return bin(sum_nums)[2:] if sum_nums % 2 != 0 else hex(sum_nums)[2:]