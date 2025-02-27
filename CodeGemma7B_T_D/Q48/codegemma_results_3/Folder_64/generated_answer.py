def return_binary_or_hexa(the_tuple):
    a, b = (the_tuple[0], the_tuple[5])
    sum_missing = sum(range(a + 1, b)) - sum(the_tuple[0:6])
    return bin(sum_missing)[2:] if sum_missing % 2 else hex(sum_missing)[2:].upper()