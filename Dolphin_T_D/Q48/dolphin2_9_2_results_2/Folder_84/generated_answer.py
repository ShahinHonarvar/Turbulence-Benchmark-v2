def return_binary_or_hexa(integer_tuple):
    a = integer_tuple[32]
    b = integer_tuple[44]
    sum_range = sum(range(a + 1, b))
    sum_tuple = sum(integer_tuple[32:45])
    if sum_range == sum_tuple:
        return ''
    else:
        sum_range = sum_range - sum_tuple
        if sum_range % 2 == 0:
            return hex(sum_range)[2:]
        else:
            return bin(sum_range)[2:]