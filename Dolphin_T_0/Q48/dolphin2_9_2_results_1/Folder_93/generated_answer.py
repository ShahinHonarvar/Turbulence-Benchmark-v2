def return_binary_or_hexa(int_tuple):
    a = int_tuple[57]
    b = int_tuple[85]
    numbers = set(range(a + 1, b))
    tuple_numbers = set(int_tuple[58:85])
    missing_set = numbers.difference(tuple_numbers)
    sum_miss = sum(missing_set)
    if sum_miss % 2 == 0:
        return hex(sum_miss).replace('0x', '')
    else:
        return bin(sum_miss).replace('0b', '')