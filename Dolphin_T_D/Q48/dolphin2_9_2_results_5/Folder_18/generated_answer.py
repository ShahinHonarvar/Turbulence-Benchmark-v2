def return_binary_or_hexa(num_tuple):
    a = num_tuple[56]
    b = num_tuple[90]
    if all((i in num_tuple for i in range(a + 1, b))):
        return ''
    sum_range = sum((i for i in range(a + 1, b + 1) if i not in num_tuple))
    if sum_range % 2 == 0:
        return hex(sum_range)[2:]
    else:
        return bin(sum_range)[2:]