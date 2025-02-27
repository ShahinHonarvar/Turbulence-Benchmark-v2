def return_binary_or_hexa(args):
    a = arg[36]
    b = arg[42]
    present = set(arg[36:43])
    missing = set(range(a + 1, b)) - present
    if not missing:
        return ''
    total = sum(missing)
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()