def return_binary_or_hexa(num_tuple):
    a = num_tuple[13]
    b = num_tuple[35]
    if a > b:
        return ''
    missing = set(range(a + 1, b)) - set(num_tuple[13:36])
    total = sum(missing)
    return bin(total)[2:] if total % 2 else hex(total)[2:]