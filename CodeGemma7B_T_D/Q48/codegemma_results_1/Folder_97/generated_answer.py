def return_binary_or_hexa(num_tuple):
    a = num_tuple[34]
    b = num_tuple[69]
    not_present = set(range(a + 1, b)) - set(num_tuple[34:69])
    return bin(sum(not_present))[2:] if len(not_present) % 2 else hex(sum(not_present))[2:].upper()